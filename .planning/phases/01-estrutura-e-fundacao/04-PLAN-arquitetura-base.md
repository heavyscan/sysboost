---
id: "1.4"
phase: 1
wave: 2
title: "Criar arquitetura base: módulos core, logging e entry point"
depends_on: ["1.1", "1.2"]
files_modified:
  - "src/core/detector.py"
  - "src/core/optimizer.py"
  - "src/core/monitor.py"
  - "src/core/benchmark.py"
  - "src/core/revert.py"
  - "src/core/logger.py"
  - "src/ui/app.py"
  - "main.py"
autonomous: true
requirements:
  - RF-01
  - RF-02
  - RF-07
  - RNF-01
  - RNF-02
---

# Plano 1.4 — Arquitetura Base: Módulos Core, Logging e Entry Point

## Objetivo

Implementar os esqueletos funcionais dos módulos core com interfaces bem definidas, sistema de logging estruturado, e o entry point da aplicação. Estes módulos serão preenchidos nas fases subsequentes — o objetivo aqui é definir as interfaces/contratos que todas as fases futuras vão implementar.

## Contexto

**Princípio:** Definir contratos (interfaces, dataclasses, tipos) antes de implementar. As fases 2-6 vão preencher as implementações reais. Nesta fase: stubs + interfaces + logging + entry point funcional.

## Tarefas

### Task 1 — Sistema de Logging Estruturado

```xml
<task id="1.4.1">
  <title>Implementar sistema de logging para o SysBoost</title>
  <read_first>
    - src/core/__init__.py (exports atuais)
    - F:\Automações\customização\.planning\REQUIREMENTS.md (RNF-01: Segurança e transparência)
  </read_first>
  <action>
    Criar `src/core/logger.py`:

    ```python
    """Sistema de logging centralizado do SysBoost."""
    import logging
    import sys
    from pathlib import Path
    from datetime import datetime
    import platformdirs

    def get_log_dir() -> Path:
        """Retorna o diretório de logs adequado para o OS atual."""
        log_dir = Path(platformdirs.user_log_dir("SysBoost", "SysBoost"))
        log_dir.mkdir(parents=True, exist_ok=True)
        return log_dir

    def setup_logging(level: int = logging.INFO, log_to_file: bool = True) -> logging.Logger:
        """
        Configura o sistema de logging.
        
        Args:
            level: Nível de logging (DEBUG, INFO, WARNING, ERROR)
            log_to_file: Se True, salva logs em arquivo no diretório do usuário
            
        Returns:
            Logger raiz configurado
        """
        root_logger = logging.getLogger("sysboost")
        root_logger.setLevel(level)
        
        # Formatter
        formatter = logging.Formatter(
            fmt="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        
        # Console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        root_logger.addHandler(console_handler)
        
        # File handler
        if log_to_file:
            log_file = get_log_dir() / f"sysboost_{datetime.now().strftime('%Y%m%d')}.log"
            file_handler = logging.FileHandler(log_file, encoding="utf-8")
            file_handler.setFormatter(formatter)
            root_logger.addHandler(file_handler)
        
        return root_logger

    def get_logger(name: str) -> logging.Logger:
        """Retorna um logger filho do logger raiz do SysBoost."""
        return logging.getLogger(f"sysboost.{name}")
    ```
  </action>
  <acceptance_criteria>
    - `src/core/logger.py` existe
    - Arquivo contém `def setup_logging(`
    - Arquivo contém `def get_logger(name: str)`
    - Arquivo contém `platformdirs.user_log_dir`
    - Executar `python -c "from src.core.logger import get_logger; print('OK')"` retorna `OK`
  </acceptance_criteria>
</task>
```

### Task 2 — Contratos dos Módulos Core (dataclasses e interfaces)

```xml
<task id="1.4.2">
  <title>Definir dataclasses e contratos dos módulos core</title>
  <read_first>
    - src/core/__init__.py
    - F:\Automações\customização\.planning\REQUIREMENTS.md (RF-01 a RF-09)
  </read_first>
  <action>
    Criar `src/core/types.py` com todos os tipos compartilhados:

    ```python
    """Tipos, dataclasses e enums compartilhados entre módulos core."""
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
        vendor: str  # "Intel", "AMD", "ARM", "Apple"
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
        ram_type: str = "Unknown"  # DDR4, DDR5, LPDDR5
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
        vendor: str  # "NVIDIA", "AMD", "Intel", "Apple"
        vram_mb: Optional[int] = None

    @dataclass
    class NetworkInfo:
        adapters: list[str] = field(default_factory=list)
        connection_type: str = "Unknown"  # Ethernet, WiFi, etc.

    @dataclass
    class HardwareProfile:
        os_name: OS
        os_version: str
        architecture: str
        cpu: CPUInfo
        ram: RAMInfo
        disks: list[DiskInfo]
        gpus: list[GPUInfo]
        network: NetworkInfo
        is_elevated: bool  # True se rodando como admin/root

    @dataclass
    class HealthScore:
        overall: int  # 0–100
        cpu: int
        ram: int
        disk: int
        network: int
        services: int

    @dataclass
    class OptimizationRecord:
        """Registro de uma otimização aplicada (para revert)."""
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
        """Snapshot do estado do sistema em um momento."""
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
        """Resultado de um benchmark sintético."""
        cpu_score: float      # operações/segundo normalizadas
        ram_bandwidth_mbs: float
        disk_read_mbs: float
        disk_write_mbs: float
        timestamp: float = 0.0
    ```

    Atualizar `src/core/__init__.py` para exportar os tipos:
    ```python
    from .types import (
        OS, DiskType, OptimizationStatus,
        CPUInfo, RAMInfo, DiskInfo, GPUInfo, NetworkInfo,
        HardwareProfile, HealthScore, OptimizationRecord,
        MonitorSnapshot, BenchmarkResult,
    )
    from .logger import get_logger, setup_logging
    ```
  </action>
  <acceptance_criteria>
    - `src/core/types.py` existe
    - Arquivo contém `class OS(Enum):`
    - Arquivo contém `class HardwareProfile:`
    - Arquivo contém `class OptimizationRecord:`
    - Arquivo contém `class MonitorSnapshot:`
    - Arquivo contém `class BenchmarkResult:`
    - Executar `python -c "from src.core.types import HardwareProfile, OS, HealthScore; print('OK')"` retorna `OK`
  </acceptance_criteria>
</task>
```

### Task 3 — Entry Point e App Stub

```xml
<task id="1.4.3">
  <title>Criar entry point main.py e stub da App</title>
  <read_first>
    - src/core/logger.py (após Task 1.4.1)
    - src/core/types.py (após Task 1.4.2)
    - src/ui/app.py (stub atual)
  </read_first>
  <action>
    Criar `main.py` na raiz do projeto:

    ```python
    #!/usr/bin/env python3
    """Entry point do SysBoost."""
    import sys
    import os

    # Adicionar raiz ao path para permitir `import src.*`
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

    def main():
        from src.core.logger import setup_logging
        import logging
        
        logger = setup_logging(level=logging.INFO)
        logger.info("Iniciando SysBoost v0.1.0")
        
        try:
            from src.ui.app import App
            app = App()
            app.mainloop()
        except ImportError as e:
            logger.error(f"Falha ao importar dependências: {e}")
            logger.error("Execute: pip install -r requirements.txt")
            sys.exit(1)
        except Exception as e:
            logger.exception(f"Erro crítico ao iniciar: {e}")
            sys.exit(1)

    if __name__ == "__main__":
        main()
    ```

    Atualizar `src/ui/app.py` com stub funcional:

    ```python
    """Aplicação principal do SysBoost — Dashboard Visual."""
    import customtkinter as ctk
    from src.core.logger import get_logger
    from src.i18n import init as i18n_init, t

    logger = get_logger("ui.app")

    # Configuração visual padrão
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    class App(ctk.CTk):
        """Janela principal do SysBoost."""

        def __init__(self):
            super().__init__()
            i18n_init()  # detecta locale automaticamente
            
            self.title(t("app.title"))
            self.geometry("1100x700")
            self.minsize(900, 600)
            
            self._setup_ui()
            logger.info("App inicializada")

        def _setup_ui(self):
            """Configura layout inicial (placeholder até Fase 3)."""
            label = ctk.CTkLabel(
                self,
                text=t("app.loading"),
                font=ctk.CTkFont(size=24, weight="bold")
            )
            label.pack(expand=True)

    def main():
        """Entry point chamado pelo pyproject.toml [scripts]."""
        app = App()
        app.mainloop()
    ```
  </action>
  <acceptance_criteria>
    - `main.py` existe na raiz do projeto
    - `main.py` contém `def main():`
    - `main.py` contém `from src.ui.app import App`
    - `src/ui/app.py` contém `class App(ctk.CTk):`
    - `src/ui/app.py` contém `ctk.set_appearance_mode("dark")`
    - `src/ui/app.py` contém `def main():`
    - Executar `python -c "from src.ui.app import App; print('App importável OK')"` retorna OK (mesmo sem display)
  </acceptance_criteria>
</task>
```

## Must-Haves

- [ ] `src/core/logger.py` com `setup_logging()` e `get_logger()`
- [ ] `src/core/types.py` com todos os dataclasses: `HardwareProfile`, `HealthScore`, `OptimizationRecord`, `MonitorSnapshot`, `BenchmarkResult`
- [ ] `main.py` funcional com tratamento de erro adequado
- [ ] `src/ui/app.py` stub com dark mode e i18n integrado
- [ ] `src/core/__init__.py` exportando todos os tipos
