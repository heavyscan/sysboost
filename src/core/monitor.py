"""System resources monitor core."""
import psutil
import time
from .types import MonitorSnapshot

class SystemMonitor:
    """Handles real-time system metrics collection."""

    def __init__(self):
        self.last_net_io = psutil.net_io_counters()
        self.last_disk_io = psutil.disk_io_counters()
        self.last_time = time.time()

    def get_snapshot(self) -> MonitorSnapshot:
        """Captures a snapshot of current system usage."""
        current_time = time.time()
        elapsed = current_time - self.last_time
        
        # CPU
        cpu_percent = psutil.cpu_percent()
        cpu_per_core = psutil.cpu_percent(percpu=True)
        
        # RAM
        mem = psutil.virtual_memory()
        
        # Disk I/O (MB/s)
        disk_io = psutil.disk_io_counters()
        read_mbs = ((disk_io.read_bytes - self.last_disk_io.read_bytes) / (1024 * 1024)) / elapsed if elapsed > 0 else 0
        write_mbs = ((disk_io.write_bytes - self.last_disk_io.write_bytes) / (1024 * 1024)) / elapsed if elapsed > 0 else 0
        
        # Net I/O (KB/s)
        net_io = psutil.net_io_counters()
        up_kbs = ((net_io.bytes_sent - self.last_net_io.bytes_sent) / 1024) / elapsed if elapsed > 0 else 0
        down_kbs = ((net_io.bytes_recv - self.last_net_io.bytes_recv) / 1024) / elapsed if elapsed > 0 else 0
        
        # Temperature (Best effort)
        temp = None
        try:
            temps = psutil.sensors_temperatures()
            if "coretemp" in temps:
                temp = temps["coretemp"][0].current
            elif "package id 0" in temps: # alternate naming
                 temp = temps["package id 0"][0].current
        except:
            pass

        # Update last state
        self.last_net_io = net_io
        self.last_disk_io = disk_io
        self.last_time = current_time

        return MonitorSnapshot(
            timestamp=current_time,
            cpu_percent=cpu_percent,
            cpu_per_core=cpu_per_core,
            ram_percent=mem.percent,
            ram_available_gb=mem.available / (1024**3),
            disk_read_mbs=round(read_mbs, 2),
            disk_write_mbs=round(write_mbs, 2),
            net_upload_kbs=round(up_kbs, 2),
            net_download_kbs=round(down_kbs, 2),
            cpu_temp_c=temp
        )
