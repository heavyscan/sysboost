"""HardwareDetector — stub for Phase 2 implementation."""
from .logger import get_logger
from .types import HardwareProfile, HealthScore

logger = get_logger("core.detector")


class HardwareDetector:
    """Detects and inventories hardware and OS information.

    Full implementation in Phase 2.
    This stub defines the interface consumed by Phase 3+ modules.
    """

    def detect(self) -> HardwareProfile:
        """Detect hardware and return a complete profile.

        Returns:
            HardwareProfile with all detected hardware info.

        Raises:
            RuntimeError: If detection fails critically.
        """
        raise NotImplementedError("Implemented in Phase 2")

    def calculate_health_score(self, profile: HardwareProfile) -> HealthScore:
        """Calculate optimization health score from a hardware profile.

        Returns:
            HealthScore with overall and per-category scores (0-100).
        """
        raise NotImplementedError("Implemented in Phase 2")
