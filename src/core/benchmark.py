"""System benchmark engines for SysBoost."""
import time
import threading
import os
import json
from pathlib import Path
import platformdirs

class CPUBenchmark:
    """Measures CPU processing power using mathematical stress tests."""

    def __init__(self, duration=5):
        self.duration = duration
        self.iterations = 0
        self.running = False

    def _stress_task(self):
        """Heavy mathematical task (calculation of primes)."""
        count = 0
        while self.running:
            # Simple prime check logic for stress
            n = 1000000
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    pass
            count += 1
        self.iterations += count

    def run(self, multi_core=True) -> int:
        """Runs the benchmark and returns a score."""
        self.iterations = 0
        self.running = True
        
        num_threads = os.cpu_count() if multi_core else 1
        threads = []
        
        for _ in range(num_threads):
            t = threading.Thread(target=self._stress_task)
            threads.append(t)
            t.start()
            
        time.sleep(self.duration)
        self.running = False
        
        for t in threads:
            t.join()
            
        # Score calculation (normalized)
        score = int(self.iterations / 1000)
        return score

class DiskBenchmark:
    """Measures disk read and write speeds."""

    def __init__(self, file_size_mb=100):
        self.file_size_mb = file_size_mb
        self.test_file = Path("disk_bench_test.tmp")

    def run(self) -> tuple[float, float]:
        """Runs write/read tests and returns (write_speed, read_speed) in MB/s."""
        data = os.urandom(1024 * 1024) # 1MB of random data
        
        # Write test
        start_time = time.time()
        with open(self.test_file, "wb") as f:
            for _ in range(self.file_size_mb):
                f.write(data)
                f.flush()
                os.fsync(f.fileno())
        write_duration = time.time() - start_time
        write_speed = self.file_size_mb / write_duration
        
        # Read test
        start_time = time.time()
        with open(self.test_file, "rb") as f:
            while f.read(1024 * 1024):
                pass
        read_duration = time.time() - start_time
        read_speed = self.file_size_mb / read_duration
        
        # Cleanup
        if self.test_file.exists():
            self.test_file.unlink()
            
        return round(write_speed, 2), round(read_speed, 2)

class BenchmarkManager:
    """Manages execution and persistence of benchmarks."""

    def __init__(self):
        self.data_dir = Path(platformdirs.user_data_dir("SysBoost", "SysBoost"))
        self.history_file = self.data_dir / "benchmarks.json"

    def save_result(self, cpu_score, disk_write, disk_read):
        """Saves a benchmark result to JSON."""
        history = self.get_history()
        
        result = {
            "timestamp": time.time(),
            "cpu_score": cpu_score,
            "disk_write_mbs": disk_write,
            "disk_read_mbs": disk_read
        }
        
        history.append(result)
        
        try:
            with open(self.history_file, "w") as f:
                json.dump(history, f, indent=4)
        except Exception as e:
            print(f"Error saving benchmark: {e}")

    def get_history(self) -> list[dict]:
        """Loads benchmark history."""
        if self.history_file.exists():
            try:
                with open(self.history_file, "r") as f:
                    return json.load(f)
            except:
                pass
        return []
