"""Optimization history and revert manager."""
import json
import os
from pathlib import Path
from datetime import datetime
import platformdirs
from .types import OptimizationRecord, OptimizationStatus
from .logger import get_logger

logger = get_logger("revert")

class HistoryManager:
    """Manages the persistence of applied optimizations."""

    def __init__(self):
        self.data_dir = Path(platformdirs.user_data_dir("SysBoost", "SysBoost"))
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.history_file = self.data_dir / "history.json"
        self.history = self._load_history()

    def _load_history(self) -> list[dict]:
        """Loads history from JSON file."""
        if self.history_file.exists():
            try:
                with open(self.history_file, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception as e:
                print(f"Error loading history: {e}")
        return []

    def save_history(self):
        """Saves current history to JSON file."""
        try:
            with open(self.history_file, "w", encoding="utf-8") as f:
                json.dump(self.history, f, indent=4, default=str)
        except Exception as e:
            print(f"Error saving history: {e}")

    def add_record(self, record: OptimizationRecord):
        """Adds a new optimization record to history."""
        # Convert dataclass to dict for JSON serialization
        record_dict = {
            "id": record.id,
            "name": record.name,
            "category": record.category,
            "applied_at": record.applied_at.isoformat(),
            "before_value": record.before_value,
            "after_value": record.after_value,
            "revert_data": record.revert_data,
            "status": record.status.value
        }
        self.history.append(record_dict)
        self.save_history()

    def get_history(self) -> list[dict]:
        """Returns the full history."""
        return self.history

    def revert_optimization(self, record_id: str) -> bool:
        """Reverts a specific optimization by its ID."""
        from .optimizer import ScoreEngine
        
        # Find the record
        record = next((r for r in self.history if r["id"] == record_id), None)
        if not record:
            logger.error(f"Registro {record_id} não encontrado.")
            return False

        success = False
        revert_data = record["revert_data"]
        
        try:
            if "win_svc_" in record_id:
                # Service Revert
                service = revert_data["service"]
                start_type = revert_data["original_start"]
                success, _ = ScoreEngine.run_command(f"sc config {service} start={start_type}")
                ScoreEngine.run_command(f"sc start {service}")
            
            elif record_id == "win_power_plan":
                # Power Plan Revert
                before_guid = revert_data["before_guid"]
                success, _ = ScoreEngine.run_command(f"powercfg /setactive {before_guid}")
            
            elif record_id == "win_visual_fx":
                # Visual FX Revert
                key = revert_data["key_path"]
                val = revert_data["value_name"]
                orig = revert_data["original_value"]
                success, _ = ScoreEngine.run_command(f'reg add "{key}" /v {val} /t REG_DWORD /d {orig} /f')
            
            elif "win_ntfs" in record_id or "win_game" in record_id:
                # Registry Tweak Revert
                key = revert_data["key"]
                val = revert_data["value"]
                orig = revert_data["original"]
                success, _ = ScoreEngine.run_command(f'reg add "{key}" /v {val} /t REG_DWORD /d {orig} /f')
            
            elif record_id == "lin_cpu_governor":
                # Linux Governor Revert
                cmd = revert_data["cmd"]
                success, _ = ScoreEngine.run_command(cmd)
            
            elif "lin_sysctl" in record_id or record_id == "lin_net_bbr":
                # Linux Sysctl Revert
                cmds = revert_data["cmds"]
                success_all = True
                for c in cmds:
                    s, _ = ScoreEngine.run_command(c)
                    if not s: success_all = False
                success = success_all
            
            elif record_id == "lin_zram":
                # Linux ZRAM Revert
                cmds = revert_data["cmds"]
                for c in cmds:
                    ScoreEngine.run_command(c)
                success = True
            
            elif "mac_" in record_id:
                # macOS Revert (defaults, mdutil, etc)
                cmd = revert_data["cmd"]
                success, _ = ScoreEngine.run_command(cmd)

            if success:


                record["status"] = OptimizationStatus.REVERTED.value
                self.save_history()
                logger.info(f"Otimização revertida: {record['name']}")
                return True
                
        except Exception as e:
            logger.error(f"Erro ao reverter {record_id}: {e}")
            
        return False

