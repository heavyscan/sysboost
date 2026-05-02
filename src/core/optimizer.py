"""Motor central de otimizações e cálculo de score."""
from .types import HardwareProfile, HealthScore, DiskType, OptimizationRecord, OptimizationStatus
from .logger import get_logger
from .revert import HistoryManager
import subprocess
from datetime import datetime

logger = get_logger("optimizer.score")

class ScoreEngine:
    """Calcula o Health Score do sistema baseado no Hardware e Estado."""

    @staticmethod
    def calculate_score(profile: 'HardwareProfile') -> 'HealthScore':
        """Calcula a pontuação atual baseada no profile."""
        cpu_score = ScoreEngine._score_cpu(profile)
        ram_score = ScoreEngine._score_ram(profile)
        disk_score = ScoreEngine._score_disk(profile)
        net_score = 50  # Base fixa, requer testes reais para melhorar
        services_score = 50  # Base fixa até termos o módulo de serviços
        
        # Média ponderada simplificada
        overall = int((cpu_score * 0.3) + (ram_score * 0.3) + (disk_score * 0.2) + (net_score * 0.1) + (services_score * 0.1))
        
        return HealthScore(
            overall=min(max(overall, 0), 100),
            cpu=cpu_score,
            ram=ram_score,
            disk=disk_score,
            network=net_score,
            services=services_score
        )

    @staticmethod
    def _score_cpu(profile: 'HardwareProfile') -> int:
        score = 50
        if profile.cpu.physical_cores >= 8:
            score += 30
        elif profile.cpu.physical_cores >= 4:
            score += 15
        if profile.cpu.base_freq_mhz > 3000:
            score += 20
        return min(score, 100)

    @staticmethod
    def _score_ram(profile: 'HardwareProfile') -> int:
        score = 40
        if profile.ram.total_gb >= 16:
            score += 40
        elif profile.ram.total_gb >= 8:
            score += 20
        
        if profile.ram.used_percent < 50:
            score += 20
        elif profile.ram.used_percent > 85:
            score -= 20
            
        return min(max(score, 0), 100)

    @staticmethod
    def _score_disk(profile: 'HardwareProfile') -> int:
        if not profile.disks:
            return 50
            
        # Pontua baseado no disco do sistema (assumindo o primeiro)
        main_disk = profile.disks[0]
        if main_disk.disk_type == DiskType.NVME:
            return 95
        elif main_disk.disk_type == DiskType.SSD:
            return 80
        else:
            return 40

    @staticmethod
    def run_command(command: str) -> tuple[bool, str]:
        """Helper to run shell commands."""
        try:
            result = subprocess.run(
                command, 
                shell=True, 
                capture_output=True, 
                text=True, 
                check=False
            )
            if result.returncode == 0:
                return True, result.stdout.strip()
            return False, result.stderr.strip()
        except Exception as e:
            return False, str(e)

class WindowsOptimizer:
    """Handles Windows-specific optimizations."""

    def __init__(self):
        self.history = HistoryManager()
        self.logger = get_logger("optimizer.windows")

    def _record_optimization(self, id: str, name: str, category: str, before: str, after: str, revert_data: dict):
        """Helper to record an optimization in history."""
        record = OptimizationRecord(
            id=id,
            name=name,
            category=category,
            applied_at=datetime.now(),
            before_value=before,
            after_value=after,
            revert_data=revert_data,
            status=OptimizationStatus.APPLIED
        )
        self.history.add_record(record)
        self.logger.info(f"Otimização aplicada: {name}")

    def optimize_power_plan(self) -> bool:
        """Sets the power plan to High Performance."""
        # GUID for High Performance: e9a42b02-d5df-448d-aa00-03f14749eb61
        high_perf_guid = "e9a42b02-d5df-448d-aa00-03f14749eb61"
        
        # Get current active plan
        success, output = ScoreEngine.run_command("powercfg /getactivescheme")
        before_guid = output.split(":")[1].split("(")[0].strip() if success else "unknown"
        
        if high_perf_guid in before_guid:
            self.logger.info("Plano de energia já está em Alto Desempenho.")
            return True

        # Use SCHEME_MIN (High Performance alias)
        success, _ = ScoreEngine.run_command("powercfg /s SCHEME_MIN")
        
        if success:
            self._record_optimization(
                id="win_power_plan",
                name="High Performance Power Plan",
                category="Power",
                before=before_guid,
                after="SCHEME_MIN",
                revert_data={"before_guid": before_guid}
            )
            return True
        return False

    def disable_unused_services(self) -> dict[str, bool]:
        """Disables SysMain and Windows Search services."""
        services = ["SysMain", "WSearch"]
        results = {}
        
        for service in services:
            # Check current status
            success, output = ScoreEngine.run_command(f"sc query {service}")
            is_running = "RUNNING" in output if success else False
            
            # Stop and disable
            ScoreEngine.run_command(f"sc stop {service}")
            success, _ = ScoreEngine.run_command(f"sc config {service} start=disabled")
            
            if success:
                self._record_optimization(
                    id=f"win_svc_{service.lower()}",
                    name=f"Disable {service} Service",
                    category="Services",
                    before="running/enabled" if is_running else "stopped/enabled",
                    after="disabled",
                    revert_data={"service": service, "original_start": "auto"} # generic auto for revert
                )
                results[service] = True
            else:
                results[service] = False
        
        return results

    def optimize_visual_effects(self) -> bool:
        """Adjusts Windows for best performance (disables animations)."""
        key_path = r"HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\VisualEffects"
        
        # Get original value
        success, output = ScoreEngine.run_command(f'reg query "{key_path}" /v VisualFXSetting')
        before_val = output.split()[-1] if success else "unknown"
        
        # Set to 2 (Adjust for best performance)
        success, _ = ScoreEngine.run_command(f'reg add "{key_path}" /v VisualFXSetting /t REG_DWORD /d 2 /f')
        
        if success:
            self._record_optimization(
                id="win_visual_fx",
                name="Performance Visual Effects",
                category="UI/UX",
                before=before_val,
                after="2",
                revert_data={"key_path": key_path, "value_name": "VisualFXSetting", "original_value": before_val}
            )
            return True
        return False


    def apply_registry_tuning(self) -> dict[str, bool]:
        """Applies various registry performance tweaks."""
        tweaks = [
            {
                "id": "win_ntfs_8dot3",
                "name": "Disable NTFS 8.3 Name Creation",
                "key": r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem",
                "value": "NtfsDisable8dot3NameCreation",
                "data": "1"
            },
            {
                "id": "win_game_mode",
                "name": "Enable Game Mode",
                "key": r"HKEY_CURRENT_USER\Software\Microsoft\GameConfigStore",
                "value": "GameModeByGameDVR",
                "data": "1"
            }
        ]
        
        results = {}
        for t in tweaks:
            success, _ = ScoreEngine.run_command(f'reg add "{t["key"]}" /v {t["value"]} /t REG_DWORD /d {t["data"]} /f')
            if success:
                self._record_optimization(
                    id=t["id"],
                    name=t["name"],
                    category="System",
                    before="unknown",
                    after=t["data"],
                    revert_data={"key": t["key"], "value": t["value"], "original": "0"}
                )
            results[t["id"]] = success
            
        return results


    def optimize_pagefile(self, ram_gb: float) -> bool:
        """Sets the pagefile size based on total RAM."""
        if ram_gb < 16:
            size_mb = int(ram_gb * 1.5 * 1024)
        else:
            size_mb = 4096
            
        key = r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management"
        value = "PagingFiles"
        data = f"C:\\pagefile.sys {size_mb} {size_mb}"
        
        success, _ = ScoreEngine.run_command(f'reg add "{key}" /v {value} /t REG_MULTI_SZ /d "{data}" /f')
        
        if success:
            self._record_optimization(
                id="win_pagefile",
                name="Optimized Virtual Memory (Pagefile)",
                category="System",
                before="system_managed",
                after=f"{size_mb}MB fixed",
                revert_data={"key": key, "value": value, "original": "PagingFiles"}
            )
            return True
        return False


class LinuxOptimizer:
    """Handles Linux-specific optimizations."""

    def __init__(self):
        self.history = HistoryManager()
        self.logger = get_logger("optimizer.linux")

    def _record_optimization(self, id: str, name: str, category: str, before: str, after: str, revert_data: dict):
        """Helper to record an optimization in history."""
        record = OptimizationRecord(
            id=id,
            name=name,
            category=category,
            applied_at=datetime.now(),
            before_value=before,
            after_value=after,
            revert_data=revert_data,
            status=OptimizationStatus.APPLIED
        )
        self.history.add_record(record)
        self.logger.info(f"Otimização aplicada: {name}")

    def optimize_governor(self) -> bool:
        """Sets the CPU governor to performance for all cores."""
        # Note: Requires root. Best effort via sysfs.
        cmd = 'echo "performance" | tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor'
        success, _ = ScoreEngine.run_command(cmd)
        
        if success:
            self._record_optimization(
                id="lin_cpu_governor",
                name="CPU Performance Governor",
                category="CPU & Power",
                before="unknown",
                after="performance",
                revert_data={"cmd": 'echo "powersave" | tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor'}
            )
            return True
        return False

    def optimize_memory_params(self, ram_gb: float) -> bool:
        """Tunes swappiness and cache pressure."""
        swappiness = 10 if ram_gb >= 8 else 30
        
        cmds = [
            f"sysctl -w vm.swappiness={swappiness}",
            "sysctl -w vm.vfs_cache_pressure=50"
        ]
        
        success_all = True
        for cmd in cmds:
            s, _ = ScoreEngine.run_command(cmd)
            if not s: success_all = False
            
        if success_all:
            self._record_optimization(
                id="lin_sysctl_mem",
                name="Memory & Cache Tuning",
                category="Memory",
                before="default",
                after=f"swappiness={swappiness}, vfs_pressure=50",
                revert_data={"cmds": ["sysctl -w vm.swappiness=60", "sysctl -w vm.vfs_cache_pressure=100"]}
            )
            return True
        return False

    def optimize_network(self) -> bool:
        """Enables TCP BBR and tunes network buffers."""
        cmds = [
            "sysctl -w net.core.default_qdisc=fq",
            "sysctl -w net.ipv4.tcp_congestion_control=bbr"
        ]
        
        success_all = True
        for cmd in cmds:
            s, _ = ScoreEngine.run_command(cmd)
            if not s: success_all = False
            
        if success_all:
            self._record_optimization(
                id="lin_net_bbr",
                name="TCP BBR Acceleration",
                category="Network",
                before="default",
                after="BBR enabled",
                revert_data={"cmds": ["sysctl -w net.ipv4.tcp_congestion_control=cubic"]}
            )
            return True
        return False

    def optimize_io_scheduler(self) -> bool:
        """Optimizes I/O scheduler for SSD/HDD."""
        cmd = 'echo "mq-deadline" | tee /sys/block/*/queue/scheduler'
        success, _ = ScoreEngine.run_command(cmd)
        
        if success:
            self._record_optimization(
                id="lin_io_sched",
                name="I/O Scheduler Tuning",
                category="Disk",
                before="unknown",
                after="mq-deadline",
                revert_data={"cmd": 'echo "none" | tee /sys/block/*/queue/scheduler'}
            )
            return True
        return False

    def setup_zram(self, ram_gb: float) -> bool:
        """Sets up ZRAM for systems with low RAM."""
        if ram_gb > 8:
            return True

        cmds = [
            "modprobe zram",
            "zramctl --find --size 2G",
            "mkswap /dev/zram0",
            "swapon /dev/zram0 -p 100"
        ]
        
        success_all = True
        for cmd in cmds:
            s, _ = ScoreEngine.run_command(cmd)
            if not s: success_all = False
            
        if success_all:
            self._record_optimization(
                id="lin_zram",
                name="ZRAM Compression",
                category="Memory",
                before="disabled",
                after="enabled (2G)",
                revert_data={"cmds": ["swapoff /dev/zram0", "rmmod zram"]}
            )
            return True
        return False


class MacOSOptimizer:
    """Handles macOS-specific optimizations."""

    def __init__(self):
        self.history = HistoryManager()
        self.logger = get_logger("optimizer.macos")

    def _record_optimization(self, id: str, name: str, category: str, before: str, after: str, revert_data: dict):
        """Helper to record an optimization in history."""
        record = OptimizationRecord(
            id=id,
            name=name,
            category=category,
            applied_at=datetime.now(),
            before_value=before,
            after_value=after,
            revert_data=revert_data,
            status=OptimizationStatus.APPLIED
        )
        self.history.add_record(record)
        self.logger.info(f"Otimização aplicada: {name}")

    def optimize_spotlight(self) -> bool:
        """Disables Spotlight indexing globally."""
        success, _ = ScoreEngine.run_command("sudo mdutil -a -i off")
        if success:
            self._record_optimization(
                id="mac_spotlight",
                name="Disable Spotlight Indexing",
                category="System",
                before="on",
                after="off",
                revert_data={"cmd": "sudo mdutil -a -i on"}
            )
            return True
        return False

    def disable_app_nap(self) -> bool:
        """Disables App Nap globally."""
        cmd = "defaults write NSGlobalDomain NSAppSleepDisabled -bool YES"
        success, _ = ScoreEngine.run_command(cmd)
        if success:
            self._record_optimization(
                id="mac_app_nap",
                name="Disable App Nap",
                category="Performance",
                before="enabled",
                after="disabled",
                revert_data={"cmd": "defaults delete NSGlobalDomain NSAppSleepDisabled"}
            )
            return True
        return False

    def check_thermal_status(self) -> str:
        """Checks if the system is currently thermal throttling."""
        success, output = ScoreEngine.run_command("pmset -g thermlog")
        if success and "Note: No CPU speed limit" not in output:
            return "Throttling Active"
        return "Normal"






