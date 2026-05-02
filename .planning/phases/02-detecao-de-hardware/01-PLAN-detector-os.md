---
id: "2.1"
phase: 2
wave: 1
title: "Detector de OS: versão, arquitetura e elevação"
depends_on: []
files_modified:
  - "src/core/detector.py"
autonomous: true
requirements:
  - RF-01
---

# Plano 2.1 — Detector de OS

## Objetivo

Implementar a detecção do Sistema Operacional (Windows, Linux, macOS), sua versão, arquitetura (x86_64, ARM, etc.), build number e verificar se o processo atual possui privilégios elevados (Administrator/root).

## Tarefas

### Task 1 — Detecção do OS e Elevação

```xml
<task id="2.1.1">
  <title>Implementar detecção do Sistema Operacional e privilégios</title>
  <read_first>
    - src/core/types.py (classe OS, HardwareProfile)
    - src/core/detector.py (stub a ser atualizado)
  </read_first>
  <action>
    Atualizar/Criar `src/core/detector.py`:

    ```python
    """Engine de detecção de hardware e sistema."""
    import platform
    import os
    import ctypes
    from .types import OS
    from .logger import get_logger

    logger = get_logger("detector.os")

    class SystemDetector:
        """Classe responsável por detectar informações do sistema e hardware."""

        @staticmethod
        def get_os_type() -> OS:
            """Retorna o tipo de OS atual."""
            sys_name = platform.system().lower()
            if sys_name == "windows":
                return OS.WINDOWS
            elif sys_name == "linux":
                return OS.LINUX
            elif sys_name == "darwin":
                return OS.MACOS
            return OS.UNKNOWN

        @staticmethod
        def get_os_version() -> str:
            """Retorna a versão do OS e build number se aplicável."""
            if SystemDetector.get_os_type() == OS.WINDOWS:
                return f"{platform.release()} (Build {platform.version()})"
            elif SystemDetector.get_os_type() == OS.MACOS:
                return f"{platform.mac_ver()[0]}"
            else:
                return platform.release()

        @staticmethod
        def get_architecture() -> str:
            """Retorna a arquitetura do sistema."""
            return platform.machine()

        @staticmethod
        def is_elevated() -> bool:
            """Verifica se o processo tem privilégios de administrador/root."""
            try:
                os_type = SystemDetector.get_os_type()
                if os_type == OS.WINDOWS:
                    return ctypes.windll.shell32.IsUserAnAdmin() != 0
                else:
                    return os.geteuid() == 0
            except Exception as e:
                logger.error(f"Erro ao verificar elevação: {e}")
                return False
    ```
  </action>
  <acceptance_criteria>
    - `src/core/detector.py` importado com sucesso
    - `SystemDetector.get_os_type()` retorna enum correto
    - `SystemDetector.is_elevated()` retorna um booleano sem levantar exceções
  </acceptance_criteria>
</task>
```

## Must-Haves
- [ ] Classe `SystemDetector` criada com métodos estáticos
- [ ] Detecção de elevação funciona em múltiplos sistemas operacionais sem crashar
