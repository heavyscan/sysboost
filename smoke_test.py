"""Smoke test for SysBoost components."""
import sys
import os

def test_imports():
    print("Testing imports...")
    try:
        from src.core.detector import SystemDetector
        from src.core.worker import MetricsWorker
        from src.core.optimizer import WindowsOptimizer, LinuxOptimizer, MacOSOptimizer
        from src.core.benchmark import BenchmarkManager
        from src.core.revert import HistoryManager
        from src.plugins.manager import PluginManager
        print("OK: All imports successful.")
    except Exception as e:
        print(f"FAIL: Import failed: {e}")
        sys.exit(1)

def test_detector():
    print("Testing SystemDetector...")
    from src.core.detector import SystemDetector
    detector = SystemDetector()
    profile = detector.get_profile()
    print(f"OK: Detector profile: {profile.os_name.value} {profile.cpu.logical_cores} cores, {profile.ram.total_gb}GB RAM")

def test_history():
    print("Testing HistoryManager...")
    from src.core.revert import HistoryManager
    manager = HistoryManager()
    history = manager.get_history()
    print(f"OK: History retrieved: {len(history)} items.")

if __name__ == "__main__":
    test_imports()
    test_detector()
    test_history()
    print("\nBUILD PASSED!")
