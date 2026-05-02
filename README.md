<div align="center">

# ⚡ SysBoost

**Cross-platform system performance optimizer with visual dashboard**

[![CI](https://github.com/sysboost/sysboost/actions/workflows/ci.yml/badge.svg)](https://github.com/sysboost/sysboost/actions)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)](README.md)

[🇧🇷 Português](docs/README.pt-BR.md) · [Download](#-installation) · [Contribute](CONTRIBUTING.md)

</div>

---

## What is SysBoost?

SysBoost is an open source tool that automatically detects your machine's hardware and applies **real, deep performance optimizations** — not just temp file cleanup.

**What it actually does:**
- 🔧 Adjusts power plans, CPU governor and kernel parameters
- 💾 Optimizes virtual memory, swappiness and cache management
- 🌐 Tunes the TCP/IP stack for lower latency
- 🗑️ Disables unnecessary services with backup for full revert
- 📊 Monitors CPU, RAM, disk and temperature in real time

## Installation

### Direct download (no Python required)
Download the executable for your system from the [Releases page](https://github.com/sysboost/sysboost/releases).

| System | Download |
|--------|----------|
| Windows 10/11 | `SysBoost.exe` |
| Linux (Ubuntu/Arch/Fedora) | `SysBoost` (binary) |
| macOS 12+ | `SysBoost.app` |

> ⚠️ **Windows:** Run as Administrator for full optimizations.
> **Linux/macOS:** `sudo ./SysBoost` for kernel-level tuning.

### From source

```bash
git clone https://github.com/sysboost/sysboost.git
cd sysboost
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# .venv\Scripts\activate    # Windows
pip install -r requirements-dev.txt
pip install -e .
python main.py
```

## Optimizations Available

| Category | Windows | Linux | macOS |
|----------|:-------:|:-----:|:-----:|
| Power Plan / CPU Governor | ✅ | ✅ | ✅ |
| RAM / Swappiness | ✅ | ✅ | ✅ |
| Disk / I/O Scheduler | ✅ | ✅ | ✅ |
| Network / TCP Tuning | ✅ | ✅ | ✅ |
| Unnecessary Services | ✅ | ✅ | ✅ |
| Boot / Startup | ✅ | ✅ | ✅ |

All optimizations are **reversible** — SysBoost saves the original state before every change.

## Plugin System

SysBoost supports community plugins. Create your own:

```python
from src.plugins.base import SysBoostPlugin, OptimizationResult

class MyPlugin(SysBoostPlugin):
    name = "my-plugin"
    display_name = "My Plugin"
    description = "What it optimizes"
    supported_os = ["windows", "linux", "darwin"]

    def is_applicable(self) -> bool:
        return True

    def apply(self) -> OptimizationResult:
        # Apply your optimization here
        return OptimizationResult(success=True, message="Applied!", revert_data={...})

    def revert(self, revert_data: dict) -> OptimizationResult:
        # Restore original state
        return OptimizationResult(success=True, message="Reverted!")
```

Place in `plugins/my-plugin/__init__.py` — SysBoost auto-discovers it.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) to get started.

## License

MIT License — see [LICENSE](LICENSE) for details.
