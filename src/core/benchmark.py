"""BenchmarkEngine — stub for Phase 8 implementation."""
from .logger import get_logger
from .types import BenchmarkResult

logger = get_logger("core.benchmark")


class BenchmarkEngine:
    """Runs synthetic benchmarks to measure system performance.

    Full implementation in Phase 8.
    """

    def run(self) -> BenchmarkResult:
        """Run a full benchmark suite (CPU + RAM + Disk).

        Returns:
            BenchmarkResult with normalized scores for each subsystem.
        """
        raise NotImplementedError("Implemented in Phase 8")

    def run_cpu(self) -> float:
        """Run CPU benchmark only. Returns normalized score."""
        raise NotImplementedError("Implemented in Phase 8")

    def run_ram(self) -> float:
        """Run RAM bandwidth benchmark. Returns MB/s."""
        raise NotImplementedError("Implemented in Phase 8")

    def run_disk(self, mountpoint: str = "/") -> tuple[float, float]:
        """Run disk benchmark. Returns (read_mbs, write_mbs)."""
        raise NotImplementedError("Implemented in Phase 8")
