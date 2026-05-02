"""Example plugin — demonstrates the SysBoost plugin interface.

This plugin does NOT apply any real optimizations.
Use it as a starting point for your own plugin.
"""
from src.plugins.base import SysBoostPlugin, OptimizationResult


class ExamplePlugin(SysBoostPlugin):
    """Demonstration plugin — no real changes applied."""

    name = "example"
    display_name = "Example Plugin"
    description = "Demonstration plugin — shows the plugin API without making real changes."
    supported_os = ["windows", "linux", "darwin"]
    category = "General"
    impact = "low"

    def is_applicable(self) -> bool:
        return True

    def apply(self) -> OptimizationResult:
        return OptimizationResult(
            success=True,
            message="Example plugin applied (no real changes made).",
            before_value="original",
            after_value="optimized",
            revert_data={"placeholder": True},
        )

    def revert(self, revert_data: dict) -> OptimizationResult:
        return OptimizationResult(
            success=True,
            message="Example plugin reverted (no real changes to undo).",
        )
