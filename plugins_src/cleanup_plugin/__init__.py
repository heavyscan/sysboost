"""Example plugin for SysBoost."""
from src.plugins.base import BasePlugin
from typing import List, Dict, Any

class CleanupPlugin(BasePlugin):
    """A plugin that provides extra cleanup optimizations."""

    @property
    def id(self) -> str:
        return "com.sysboost.example.cleanup"

    @property
    def name(self) -> str:
        return "Custom Cleanup Tool"

    @property
    def description(self) -> str:
        return "Removes temporary logs and crash reports from common apps."

    @property
    def version(self) -> str:
        return "1.0.0"

    def on_load(self):
        print(f"Plugin {self.name} loaded.")

    def on_unload(self):
        print(f"Plugin {self.name} unloaded.")

    def get_optimizations(self) -> List[Dict[str, Any]]:
        return [
            {
                "id": "ext_log_cleanup",
                "name": "Clean App Logs",
                "description": "Deletes .log files from the temporary folder.",
                "category": "Cleanup"
            }
        ]
