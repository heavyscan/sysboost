"""SysBoost core package — hardware detection, optimization, monitoring and benchmarking."""
from .types import (
    OS, DiskType, OptimizationStatus,
    CPUInfo, RAMInfo, DiskInfo, GPUInfo, NetworkInfo,
    HardwareProfile, HealthScore, OptimizationRecord,
    MonitorSnapshot, BenchmarkResult,
)
from .logger import get_logger, setup_logging

__all__ = [
    # Enums
    "OS", "DiskType", "OptimizationStatus",
    # Hardware types
    "CPUInfo", "RAMInfo", "DiskInfo", "GPUInfo", "NetworkInfo",
    "HardwareProfile", "HealthScore",
    # Runtime types
    "OptimizationRecord", "MonitorSnapshot", "BenchmarkResult",
    # Logging
    "get_logger", "setup_logging",
]
