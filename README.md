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

---

## 💻 System Requirements / Requisitos de Sistema

### 🇺🇸 English — Minimum & Recommended Configuration

The architecture of **SysBoost** supports three hardware profiles depending on whether you run the standalone pre-built executable, execute from Python source, or compile native binaries via **PyInstaller**:

| Resource | 🟢 Minimum (Standalone Binary — End User) | 🟡 Intermediate (Run from Source via Python) | 🔵 Recommended (Development, Testing & Build) |
| :--- | :--- | :--- | :--- |
| **CPU** | **1 to 2 Cores** (`x86_64` / `arm64`) | **2 Cores** (`x86_64` / `arm64`) | **4+ Cores** (`x86_64` / `arm64`) |
| **RAM** | **2 GB RAM** (app footprint ~40–90 MB) | **4 GB RAM** | **8 GB+ RAM** |
| **Storage (SSD)** | **150 MB free** (binary + revert backups & logs) | **500 MB free** (Python 3.11+ venv + dependencies) | **2 GB+ SSD** (venv + `pytest` + `PyInstaller` build artifacts) |
| **GPU (Optional)** | Integrated GPU (desktop display required) | Integrated GPU (desktop display required) | Integrated or Dedicated GPU |
| **Operating System** | Windows 10/11 (64-bit), Linux (Ubuntu/Arch/Fedora), or macOS 12+ | Windows 10/11, Linux (X11/Wayland + Tk), or macOS 12+ | Windows 11, Ubuntu 24.04 LTS, or macOS 13+ |

#### 📦 Resource Usage by Architecture Component
- **Visual Dashboard & UI (`CustomTkinter` + `Pillow` + `Tkinter`)**: ~40 MB to 90 MB RAM during real-time telemetry rendering.
- **Hardware Detection & Telemetry Engine (`psutil` + OS probes)**: ~15 MB to 30 MB RAM with minimal (< 2%) CPU polling overhead.
- **Optimization & Reversible Backup Engine (Power plans, CPU governor, `sysctl`/kernel, TCP/IP, services)**: < 10 MB RAM; requires **Administrator** (`Windows`) or **`sudo`** (`Linux`/`macOS`) privileges for full system-level tuning.
- **Binary Packaging (`PyInstaller` + `sysboost.spec` / `scripts/build.ps1`)**: ~300 MB to 800 MB RAM during standalone executable compilation.

#### 🛠️ Software Dependencies
- **Direct Executable**: No Python required (`SysBoost.exe`, `SysBoost` binary, or `SysBoost.app`); elevated privileges recommended for kernel/service tuning.
- **From Source (`requirements.txt` / `pyproject.toml`)**: `Python >= 3.11` (`3.11` / `3.12`), `customtkinter >= 5.2.0`, `psutil >= 5.9.0`, `platformdirs >= 4.0.0`, `pillow >= 10.0.0` (plus `python3-tk` on Linux).
- **Development & Build (`requirements-dev.txt`)**: `pytest >= 7.4.0`, `pytest-cov >= 4.1.0`, `ruff >= 0.1.0`, `pyinstaller >= 6.0.0`, `pre-commit >= 3.5.0`.

### 🇧🇷 Português (BR) — Configuração Mínima & Recomendada

A arquitetura do **SysBoost** permite operar em três perfis de hardware, dependendo se você utiliza o executável pré-compilado, executa a partir do código-fonte em Python ou compila binários nativos com **PyInstaller**:

| Recurso | 🟢 Mínimo (Executável Pronto — Usuário Final) | 🟡 Intermediário (Execução via Código-Fonte Python) | 🔵 Recomendado (Desenvolvimento, Testes & Build) |
| :--- | :--- | :--- | :--- |
| **CPU** | **1 a 2 Núcleos** (`x86_64` / `arm64`) | **2 Núcleos** (`x86_64` / `arm64`) | **4+ Núcleos** (`x86_64` / `arm64`) |
| **Memória RAM** | **2 GB RAM** (consumo do app ~40–90 MB) | **4 GB RAM** | **8 GB+ RAM** |
| **Armazenamento (SSD)** | **150 MB livres** (executável + backups de reversão e logs) | **500 MB livres** (venv Python 3.11+ + dependências) | **2 GB+ SSD** (venv + `pytest` + artefatos de build `PyInstaller`) |
| **GPU (Opcional)** | GPU Integrada (requer ambiente gráfico) | GPU Integrada (requer ambiente gráfico) | GPU Integrada ou Dedicada |
| **Sistema Operacional** | Windows 10/11 (64-bit), Linux (Ubuntu/Arch/Fedora) ou macOS 12+ | Windows 10/11, Linux (X11/Wayland + Tk) ou macOS 12+ | Windows 11, Ubuntu 24.04 LTS ou macOS 13+ |

#### 📦 Consumo por Componente da Arquitetura
- **Dashboard Visual & Interface (`CustomTkinter` + `Pillow` + `Tkinter`)**: ~40 MB a 90 MB de RAM durante a renderização da telemetria em tempo real.
- **Motor de Detecção de Hardware & Telemetria (`psutil` + sensores do SO)**: ~15 MB a 30 MB de RAM com overhead mínimo (< 2% de CPU).
- **Motor de Otimização & Reversão (Planos de energia, CPU governor, `sysctl`/kernel, TCP/IP, serviços)**: < 10 MB de RAM; requer privilégios de **Administrador** (`Windows`) ou **`sudo`** (`Linux`/`macOS`) para ajustes em nível de kernel e serviços.
- **Empacotamento de Binários (`PyInstaller` + `sysboost.spec` / `scripts/build.ps1`)**: ~300 MB a 800 MB de RAM durante a compilação do executável standalone.

#### 🛠️ Dependências de Software
- **Executável Direto**: Não requer Python (`SysBoost.exe`, binário `SysBoost` ou `SysBoost.app`); recomenda-se execução elevada para otimizações completas.
- **A partir do Código-Fonte (`requirements.txt` / `pyproject.toml`)**: `Python >= 3.11` (`3.11` / `3.12`), `customtkinter >= 5.2.0`, `psutil >= 5.9.0`, `platformdirs >= 4.0.0`, `pillow >= 10.0.0` (e `python3-tk` no Linux).
- **Desenvolvimento & Build (`requirements-dev.txt`)**: `pytest >= 7.4.0`, `pytest-cov >= 4.1.0`, `ruff >= 0.1.0`, `pyinstaller >= 6.0.0`, `pre-commit >= 3.5.0`.

---

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

## Development & Build

If you want to generate the executable binary for distribution:

### Windows
```powershell
./scripts/build.ps1
```

### Linux / macOS
```bash
pyinstaller sysboost.spec
```

The resulting binary will be located in the `dist/` folder.

## License

MIT License — see [LICENSE](LICENSE) for details.
