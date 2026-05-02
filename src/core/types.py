"""SysBoost shared types, dataclasses and enums used across all core modules."""
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
import datetime


class OS(Enum):
    WINDOWS = "windows"
    LINUX = "linux"
    MACOS = "darwin"
    UNKNOWN = "unknown"


class DiskType(Enum):
    NVME = "nvme"
    SSD = "ssd"
    HDD = "hdd"
    UNKNOWN = "unknown"


class OptimizationStatus(Enum):
    PENDING = "pending"
    APPLIED = "applied"
    FAILED = "failed"
    INCOMPATIBLE = "incompatible"
    REVERTED = "reverted"


@dataclass
class CPUInfo:
    model: str
    vendor: str           # "Intel", "AMD", "ARM", "Apple"
    physical_cores: int
    logical_cores: int
    base_freq_mhz: float
    max_freq_mhz: float
    cache_l3_mb: Optional[float] = None


@dataclass
class RAMInfo:
    total_gb: float
    available_gb: float
    used_percent: float
    ram_type: str = "Unknown"   # DDR4, DDR5, LPDDR5
    freq_mhz: Optional[int] = None


@dataclass
class DiskInfo:
    device: str
    mountpoint: str
    disk_type: DiskType
    total_gb: float
    free_gb: float
    model: str = "Unknown"


@dataclass
class GPUInfo:
    model: str
    vendor: str   # "NVIDIA", "AMD", "Intel", "Apple"
    vram_mb: Optional[int] = None


@dataclass
class NetworkInfo:
    adapters: list[str] = field(default_factory=list)
    connection_type: str = "Unknown"   # Ethernet, WiFi


@dataclass
class HardwareProfile:
    """Complete hardware and OS profile for the current machine."""
    os_name: OS
    os_version: str
    architecture: str
    cpu: CPUInfo
    ram: RAMInfo
    disks: list[DiskInfo]
    gpus: list[GPUInfo]
    network: NetworkInfo
    is_elevated: bool     # True if running as admin/root


@dataclass
class HealthScore:
    """System health score broken down by category (0-100)."""
    overall: int
    cpu: int
    ram: int
    disk: int
    network: int
    services: int


@dataclass
class OptimizationRecord:
    """Record of an applied optimization (used for history and revert)."""
    id: str
    name: str
    category: str
    applied_at: datetime.datetime
    before_value: str
    after_value: str
    revert_data: dict
    status: OptimizationStatus = OptimizationStatus.APPLIED


@dataclass
class MonitorSnapshot:
    """System metrics snapshot at a point in time."""
    timestamp: float
    cpu_percent: float
    cpu_per_core: list[float]
    ram_percent: float
    ram_available_gb: float
    disk_read_mbs: float
    disk_write_mbs: float
    net_upload_kbs: float
    net_download_kbs: float
    cpu_temp_c: Optional[float] = None


@dataclass
class BenchmarkResult:
    """Result of a synthetic benchmark run."""
    cpu_score: float         # normalized ops/second
    ram_bandwidth_mbs: float
    disk_read_mbs: float
    disk_write_mbs: float
    timestamp: float = 0.0
