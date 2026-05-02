"""Engine de detecção de hardware e sistema."""
import platform
import os
import ctypes
from .types import OS
from .logger import get_logger

logger = get_logger("detector.os")

class SystemDetector:
    """Classe responsável por detectar informações do sistema e hardware."""

    @staticmethod
    def get_os_type() -> OS:
        """Retorna o tipo de OS atual."""
        sys_name = platform.system().lower()
        if sys_name == "windows":
            return OS.WINDOWS
        elif sys_name == "linux":
            return OS.LINUX
        elif sys_name == "darwin":
            return OS.MACOS
        return OS.UNKNOWN

    @staticmethod
    def get_os_version() -> str:
        """Retorna a versão do OS e build number se aplicável."""
        if SystemDetector.get_os_type() == OS.WINDOWS:
            return f"{platform.release()} (Build {platform.version()})"
        elif SystemDetector.get_os_type() == OS.MACOS:
            return f"{platform.mac_ver()[0]}"
        else:
            return platform.release()

    @staticmethod
    def get_architecture() -> str:
        """Retorna a arquitetura do sistema."""
        return platform.machine()

    @staticmethod
    def is_elevated() -> bool:
        """Verifica se o processo tem privilégios de administrador/root."""
        try:
            os_type = SystemDetector.get_os_type()
            if os_type == OS.WINDOWS:
                return ctypes.windll.shell32.IsUserAnAdmin() != 0
            else:
                return os.geteuid() == 0
        except Exception as e:
            logger.error(f"Erro ao verificar elevação: {e}")
            return False

    @staticmethod
    def get_cpu_info() -> 'CPUInfo':
        """Coleta informações detalhadas da CPU."""
        from .types import CPUInfo
        import platform
        import psutil

        logical_cores = psutil.cpu_count(logical=True) or 1
        physical_cores = psutil.cpu_count(logical=False) or 1
        
        freq = psutil.cpu_freq()
        base_freq = freq.current if freq else 0.0
        max_freq = freq.max if freq else 0.0

        processor_name = platform.processor()
        vendor = "Unknown"
        
        name_lower = processor_name.lower()
        if "intel" in name_lower:
            vendor = "Intel"
        elif "amd" in name_lower:
            vendor = "AMD"
        elif "apple" in name_lower:
            vendor = "Apple"
        elif "arm" in name_lower or "aarch64" in platform.machine().lower():
            vendor = "ARM"

        return CPUInfo(
            model=processor_name,
            vendor=vendor,
            physical_cores=physical_cores,
            logical_cores=logical_cores,
            base_freq_mhz=base_freq,
            max_freq_mhz=max_freq,
            cache_l3_mb=None
        )

    @staticmethod
    def get_ram_info() -> 'RAMInfo':
        """Coleta informações sobre a memória RAM do sistema."""
        from .types import RAMInfo
        import psutil

        mem = psutil.virtual_memory()
        
        total_gb = mem.total / (1024 ** 3)
        available_gb = mem.available / (1024 ** 3)
        used_percent = mem.percent
        
        return RAMInfo(
            total_gb=round(total_gb, 2),
            available_gb=round(available_gb, 2),
            used_percent=used_percent,
            ram_type="Unknown",
            freq_mhz=None
        )

    @staticmethod
    def get_disks_info() -> list['DiskInfo']:
        """Coleta informações sobre os discos do sistema."""
        from .types import DiskInfo, DiskType
        import psutil

        disks = []
        try:
            partitions = psutil.disk_partitions(all=False)
        except Exception as e:
            logger.error(f"Falha ao ler partições: {e}")
            partitions = []

        for partition in partitions:
            if partition.fstype == "" or "loop" in partition.device.lower():
                continue

            try:
                usage = psutil.disk_usage(partition.mountpoint)
            except PermissionError:
                continue
            except FileNotFoundError:
                continue

            total_gb = usage.total / (1024 ** 3)
            free_gb = usage.free / (1024 ** 3)
            
            disk_type = DiskType.UNKNOWN
            dev_lower = partition.device.lower()
            if "nvme" in dev_lower:
                disk_type = DiskType.NVME
            elif "sd" in dev_lower:
                disk_type = DiskType.SSD

            disks.append(DiskInfo(
                device=partition.device,
                mountpoint=partition.mountpoint,
                disk_type=disk_type,
                total_gb=round(total_gb, 2),
                free_gb=round(free_gb, 2),
                model="Unknown"
            ))

        return disks

    @staticmethod
    def get_gpus_info() -> list['GPUInfo']:
        """Coleta informações básicas sobre GPUs."""
        from .types import GPUInfo
        # Implementação 'best effort' multiplataforma sem bibliotecas pesadas.
        return [GPUInfo(model="Generic Display Adapter", vendor="Unknown", vram_mb=None)]

    @staticmethod
    def get_network_info() -> 'NetworkInfo':
        """Coleta informações dos adaptadores de rede."""
        from .types import NetworkInfo
        import psutil
        
        adapters = list(psutil.net_if_stats().keys())
        adapters = [a for a in adapters if not a.startswith('lo')]
        
        return NetworkInfo(
            adapters=adapters,
            connection_type="Ethernet/WiFi"
        )

    @classmethod
    def get_profile(cls) -> 'HardwareProfile':
        """Retorna o perfil de hardware completo agrupado."""
        from .types import HardwareProfile
        
        return HardwareProfile(
            os_name=cls.get_os_type(),
            os_version=cls.get_os_version(),
            architecture=cls.get_architecture(),
            cpu=cls.get_cpu_info(),
            ram=cls.get_ram_info(),
            disks=cls.get_disks_info(),
            gpus=cls.get_gpus_info(),
            network=cls.get_network_info(),
            is_elevated=cls.is_elevated()
        )
