"""SysBoost plugins base interface."""
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional
import platform


@dataclass
class OptimizationResult:
    """Result of an optimization apply or revert operation."""
    success: bool
    message: str
    before_value: Optional[str] = None
    after_value: Optional[str] = None
    revert_data: Optional[dict] = None


class SysBoostPlugin(ABC):
    """Abstract base class for all SysBoost plugins.

    To create a plugin, extend this class and implement all abstract methods.
    Place your plugin in plugins/<name>/__init__.py — SysBoost auto-discovers it.

    Example:
        class MyPlugin(SysBoostPlugin):
            name = "my-plugin"
            display_name = "My Plugin"
            description = "What it does"
            supported_os = ["windows", "linux", "darwin"]

            def is_applicable(self) -> bool:
                return True

            def apply(self) -> OptimizationResult:
                # Apply optimization, save revert data
                return OptimizationResult(success=True, message="Applied!", revert_data={...})

            def revert(self, revert_data: dict) -> OptimizationResult:
                # Restore previous state
                return OptimizationResult(success=True, message="Reverted!")
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """Unique plugin identifier (e.g. 'gaming-mode'). Used internally."""
        ...

    @property
    @abstractmethod
    def display_name(self) -> str:
        """Human-readable name shown in the UI (e.g. 'Gaming Mode')."""
        ...

    @property
    @abstractmethod
    def description(self) -> str:
        """Short description of what this plugin optimizes."""
        ...

    @property
    @abstractmethod
    def supported_os(self) -> list[str]:
        """List of supported OSes: 'windows', 'linux', 'darwin'."""
        ...

    @abstractmethod
    def is_applicable(self) -> bool:
        """Return True if this plugin can run on the current machine.

        Check for hardware requirements, permissions, etc.
        Called before apply() to avoid unnecessary errors.
        """
        ...

    @abstractmethod
    def apply(self) -> OptimizationResult:
        """Apply the optimization.

        MUST save enough state in revert_data to fully undo the change.
        MUST be idempotent — applying twice should not cause issues.
        """
        ...

    @abstractmethod
    def revert(self, revert_data: dict) -> OptimizationResult:
        """Revert the optimization using data saved by apply()."""
        ...

    def is_supported(self) -> bool:
        """Check if the current OS is in supported_os."""
        current = platform.system().lower()
        return current in [os.lower() for os in self.supported_os]

    @property
    def category(self) -> str:
        """Optional category for UI grouping. Override to customize."""
        return "General"

    @property
    def impact(self) -> str:
        """Expected impact level: 'low', 'medium', 'high'. Override to customize."""
        return "medium"
