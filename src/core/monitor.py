"""SystemMonitor — stub for Phase 3 implementation."""
from .logger import get_logger
from .types import MonitorSnapshot

logger = get_logger("core.monitor")


class SystemMonitor:
    """Collects real-time system metrics.

    Full implementation in Phase 3.
    This stub defines the interface consumed by Phase 3 dashboard.
    """

    def snapshot(self) -> MonitorSnapshot:
        """Capture a single system metrics snapshot.

        Returns:
            MonitorSnapshot with CPU, RAM, disk I/O, network and temperature data.
        """
        raise NotImplementedError("Implemented in Phase 3")

    def start_background(self, interval_seconds: float = 1.0) -> None:
        """Start background collection thread."""
        raise NotImplementedError("Implemented in Phase 3")

    def stop_background(self) -> None:
        """Stop background collection thread."""
        raise NotImplementedError("Implemented in Phase 3")

    def get_history(self, seconds: int = 60) -> list[MonitorSnapshot]:
        """Return recent history of snapshots.

        Args:
            seconds: How many seconds of history to return.
        """
        raise NotImplementedError("Implemented in Phase 3")
