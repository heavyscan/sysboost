"""Background threading worker for SysBoost."""
import threading
import time
from src.core.monitor import SystemMonitor

class MetricsWorker:
    """Worker that collects system metrics in a background thread."""

    def __init__(self, callback):
        self.callback = callback
        self.monitor = SystemMonitor()
        self.running = False
        self.thread = None

    def start(self):
        """Starts the background collection thread."""
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self._run, daemon=True)
            self.thread.start()

    def stop(self):
        """Stops the collection loop."""
        self.running = False

    def _run(self):
        """Loop that captures snapshots and calls the callback."""
        while self.running:
            try:
                snapshot = self.monitor.get_snapshot()
                self.callback(snapshot)
            except Exception as e:
                print(f"Metrics worker error: {e}")
            time.sleep(1) # Refresh rate: 1s
