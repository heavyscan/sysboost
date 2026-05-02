"""Plugin management and loading system for SysBoost."""
import os
import json
import importlib.util
from pathlib import Path
from typing import Dict, List, Type
import platformdirs
from src.plugins.base import BasePlugin
from src.core.logger import get_logger

logger = get_logger("plugins.manager")

class PluginManager:
    """Handles discovery, loading, and management of plugins."""

    def __init__(self):
        self.data_dir = Path(platformdirs.user_data_dir("SysBoost", "SysBoost"))
        self.plugins_dir = self.data_dir / "plugins"
        self.plugins_dir.mkdir(parents=True, exist_ok=True)
        
        self.loaded_plugins: Dict[str, BasePlugin] = {}

    def discover_plugins(self) -> List[Path]:
        """Finds all plugin directories in the plugins folder."""
        plugin_dirs = []
        for item in self.plugins_dir.iterdir():
            if item.is_dir() and (item / "plugin.json").exists():
                plugin_dirs.append(item)
        return plugin_dirs

    def load_plugin(self, plugin_dir: Path) -> bool:
        """Loads a plugin from its directory."""
        try:
            # Read manifest
            with open(plugin_dir / "plugin.json", "r") as f:
                manifest = json.load(f)
            
            plugin_id = manifest.get("id")
            main_file = plugin_dir / manifest.get("main_file", "__init__.py")
            class_name = manifest.get("main_class")

            if not plugin_id or not main_file.exists() or not class_name:
                logger.error(f"Invalid manifest in {plugin_dir}")
                return False

            # Dynamic import
            spec = importlib.util.spec_from_file_location(f"plugin_{plugin_id}", str(main_file))
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            # Instantiate plugin class
            plugin_class: Type[BasePlugin] = getattr(module, class_name)
            plugin_instance = plugin_class()
            
            plugin_instance.on_load()
            self.loaded_plugins[plugin_id] = plugin_instance
            
            logger.info(f"Plugin loaded: {plugin_instance.name} v{plugin_instance.version}")
            return True

        except Exception as e:
            logger.error(f"Failed to load plugin from {plugin_dir}: {e}")
            return False

    def load_all_plugins(self):
        """Discovers and loads all available plugins."""
        for p_dir in self.discover_plugins():
            self.load_plugin(p_dir)

    def unload_plugin(self, plugin_id: str):
        """Unloads a specific plugin."""
        if plugin_id in self.loaded_plugins:
            try:
                self.loaded_plugins[plugin_id].on_unload()
                del self.loaded_plugins[plugin_id]
                logger.info(f"Plugin unloaded: {plugin_id}")
            except Exception as e:
                logger.error(f"Error unloading plugin {plugin_id}: {e}")
