"""Base classes for SysBoost plugins."""
from abc import ABC, abstractmethod
from typing import List, Dict, Any

class BasePlugin(ABC):
    """Abstract base class that all plugins must inherit from."""

    def __init__(self):
        self.enabled = False

    @property
    @abstractmethod
    def id(self) -> str:
        """Unique identifier for the plugin (e.g. 'com.sysboost.cleanup')."""
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        """Human-readable name of the plugin."""
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """Brief description of what the plugin does."""
        pass

    @property
    @abstractmethod
    def version(self) -> str:
        """Plugin version string."""
        pass

    @abstractmethod
    def on_load(self):
        """Called when the plugin is loaded."""
        pass

    @abstractmethod
    def on_unload(self):
        """Called when the plugin is unloaded."""
        pass

    @abstractmethod
    def get_optimizations(self) -> List[Dict[str, Any]]:
        """Returns a list of optimization definitions provided by this plugin."""
        pass
