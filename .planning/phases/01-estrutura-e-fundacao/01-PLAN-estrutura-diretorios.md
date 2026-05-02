---
id: "1.1"
phase: 1
wave: 1
title: "Criar estrutura de diretórios do projeto"
depends_on: []
files_modified:
  - "src/__init__.py"
  - "src/core/__init__.py"
  - "src/core/detector.py"
  - "src/core/optimizer.py"
  - "src/core/monitor.py"
  - "src/core/benchmark.py"
  - "src/core/revert.py"
  - "src/ui/__init__.py"
  - "src/ui/app.py"
  - "src/ui/components/__init__.py"
  - "src/plugins/__init__.py"
  - "src/plugins/base.py"
  - "src/i18n/__init__.py"
  - "src/i18n/pt_BR.json"
  - "src/i18n/en_US.json"
  - "tests/__init__.py"
  - "tests/unit/__init__.py"
  - "tests/integration/__init__.py"
  - "docs/README.md"
  - "plugins/example/__init__.py"
  - ".gitignore"
autonomous: true
requirements:
  - RF-01
  - RF-10
---

# Plano 1.1 — Criar Estrutura de Diretórios do Projeto

## Objetivo

Criar o scaffolding completo do projeto SysBoost com todos os diretórios e arquivos `__init__.py` necessários, seguindo arquitetura modular que suporte extensão via plugins, separação clara entre core/ui/i18n e testabilidade desde o início.

## Contexto

**Projeto:** SysBoost — Otimizador de desempenho multiplataforma (Windows/Linux/macOS)
**Stack:** Python 3.11+, CustomTkinter, psutil
**Padrão:** Arquitetura em camadas (core → ui → plugins), YOLO mode

## Tarefas

### Task 1 — Criar estrutura de diretórios principal

```xml
<task id="1.1.1">
  <title>Criar árvore de diretórios do projeto</title>
  <read_first>
    - F:\Automações\customização\.planning\PROJECT.md (visão do projeto e decisões técnicas)
    - F:\Automações\customização\.planning\REQUIREMENTS.md (requisitos e escopo)
  </read_first>
  <action>
    Criar a seguinte estrutura de diretórios exatamente como especificado:

    sysboost/                          ← raiz do projeto
    ├── src/
    │   ├── __init__.py                ← versão: __version__ = "0.1.0"
    │   ├── core/
    │   │   ├── __init__.py            ← exporta: Detector, Optimizer, Monitor, Benchmark, RevertManager
    │   │   ├── detector.py            ← classe HardwareDetector (stub com docstring)
    │   │   ├── optimizer.py           ← classe OptimizerEngine (stub com docstring)
    │   │   ├── monitor.py             ← classe SystemMonitor (stub com docstring)
    │   │   ├── benchmark.py           ← classe BenchmarkEngine (stub com docstring)
    │   │   └── revert.py              ← classe RevertManager (stub com docstring)
    │   ├── ui/
    │   │   ├── __init__.py            ← exporta: App
    │   │   ├── app.py                 ← classe App(ctk.CTk) (stub)
    │   │   └── components/
    │   │       └── __init__.py        ← vazio por ora
    │   ├── plugins/
    │   │   ├── __init__.py            ← exporta: SysBoostPlugin, PluginLoader
    │   │   └── base.py                ← classe abstrata SysBoostPlugin (interface completa)
    │   └── i18n/
    │       ├── __init__.py            ← função t(key, lang=None) → str
    │       ├── pt_BR.json             ← {"app.title": "SysBoost", "app.loading": "Carregando..."}
    │       └── en_US.json             ← {"app.title": "SysBoost", "app.loading": "Loading..."}
    ├── tests/
    │   ├── __init__.py
    │   ├── unit/
    │   │   └── __init__.py
    │   └── integration/
    │       └── __init__.py
    ├── plugins/
    │   └── example/
    │       └── __init__.py            ← plugin de exemplo mínimo estendendo SysBoostPlugin
    └── docs/
        └── README.md                  ← placeholder: "# SysBoost Docs"

    Cada __init__.py com conteúdo de módulo adequado (não deixar completamente vazio onde há exportações especificadas).

    Arquivo raiz .gitignore com conteúdo:
    ```
    __pycache__/
    *.py[cod]
    *$py.class
    *.so
    .Python
    build/
    dist/
    *.egg-info/
    .eggs/
    .env
    .venv
    venv/
    ENV/
    .pytest_cache/
    .coverage
    htmlcov/
    .ruff_cache/
    *.spec
    dist-linux/
    dist-win/
    dist-mac/
    .sysboost/
    ```
  </action>
  <acceptance_criteria>
    - `src/core/__init__.py` contém `from .detector import HardwareDetector`
    - `src/plugins/base.py` contém `class SysBoostPlugin(ABC):`
    - `src/i18n/pt_BR.json` é JSON válido com chave "app.title"
    - `tests/unit/__init__.py` existe (pode estar vazio)
    - `plugins/example/__init__.py` existe
    - `.gitignore` contém `__pycache__/`
    - `src/__init__.py` contém `__version__ = "0.1.0"`
  </acceptance_criteria>
</task>
```

### Task 2 — Implementar interface base de plugins

```xml
<task id="1.1.2">
  <title>Implementar classe abstrata SysBoostPlugin</title>
  <read_first>
    - src/plugins/__init__.py (após criação pela Task 1.1.1)
    - F:\Automações\customização\.planning\REQUIREMENTS.md (RF-09: Sistema de Plugins)
  </read_first>
  <action>
    Em `src/plugins/base.py`, implementar a interface completa de plugins:

    ```python
    from abc import ABC, abstractmethod
    from dataclasses import dataclass
    from typing import Optional
    import platform

    @dataclass
    class OptimizationResult:
        success: bool
        message: str
        before_value: Optional[str] = None
        after_value: Optional[str] = None
        revert_data: Optional[dict] = None

    class SysBoostPlugin(ABC):
        """Interface base para plugins do SysBoost.
        
        Para criar um plugin, estenda esta classe e implemente
        todos os métodos abstratos.
        """

        @property
        @abstractmethod
        def name(self) -> str:
            """Nome único do plugin (ex: 'gaming-mode')."""
            ...

        @property
        @abstractmethod
        def display_name(self) -> str:
            """Nome exibido na UI (ex: 'Modo Gamer')."""
            ...

        @property
        @abstractmethod
        def description(self) -> str:
            """Descrição do que o plugin faz."""
            ...

        @property
        @abstractmethod
        def supported_os(self) -> list[str]:
            """Lista de OSes suportados: 'windows', 'linux', 'darwin'."""
            ...

        @abstractmethod
        def is_applicable(self) -> bool:
            """Retorna True se o plugin é aplicável na máquina atual."""
            ...

        @abstractmethod
        def apply(self) -> OptimizationResult:
            """Aplica a otimização. Deve ser reversível."""
            ...

        @abstractmethod
        def revert(self, revert_data: dict) -> OptimizationResult:
            """Reverte a otimização usando dados salvos por apply()."""
            ...

        def is_supported(self) -> bool:
            """Verifica se o OS atual é suportado pelo plugin."""
            current_os = platform.system().lower()
            return current_os in [os.lower() for os in self.supported_os]
    ```

    Em `plugins/example/__init__.py`, implementar plugin de exemplo mínimo:

    ```python
    from src.plugins.base import SysBoostPlugin, OptimizationResult

    class ExamplePlugin(SysBoostPlugin):
        name = "example"
        display_name = "Plugin de Exemplo"
        description = "Plugin de demonstração — não aplica nenhuma otimização real."
        supported_os = ["windows", "linux", "darwin"]

        def is_applicable(self) -> bool:
            return True

        def apply(self) -> OptimizationResult:
            return OptimizationResult(success=True, message="Exemplo aplicado (sem alterações reais)")

        def revert(self, revert_data: dict) -> OptimizationResult:
            return OptimizationResult(success=True, message="Exemplo revertido")
    ```
  </action>
  <acceptance_criteria>
    - `src/plugins/base.py` contém `class SysBoostPlugin(ABC):`
    - `src/plugins/base.py` contém `class OptimizationResult:`
    - `src/plugins/base.py` contém `def apply(self) -> OptimizationResult:`
    - `src/plugins/base.py` contém `def revert(self, revert_data: dict) -> OptimizationResult:`
    - `plugins/example/__init__.py` contém `class ExamplePlugin(SysBoostPlugin):`
    - Executar `python -c "from src.plugins.base import SysBoostPlugin, OptimizationResult; print('OK')"` retorna `OK` sem erros
  </acceptance_criteria>
</task>
```

### Task 3 — Implementar módulo de i18n

```xml
<task id="1.1.3">
  <title>Implementar sistema de internacionalização</title>
  <read_first>
    - src/i18n/__init__.py (após criação pela Task 1.1.1)
  </read_first>
  <action>
    Em `src/i18n/__init__.py`, implementar:

    ```python
    import json
    import locale
    from pathlib import Path

    _TRANSLATIONS: dict[str, dict] = {}
    _current_lang: str = "en_US"

    def _load_lang(lang: str) -> dict:
        """Carrega arquivo de tradução JSON."""
        lang_file = Path(__file__).parent / f"{lang}.json"
        if lang_file.exists():
            with open(lang_file, encoding="utf-8") as f:
                return json.load(f)
        return {}

    def init(lang: str | None = None) -> None:
        """Inicializa o sistema de i18n. Detecta locale do sistema se lang=None."""
        global _current_lang
        if lang is None:
            system_locale = locale.getdefaultlocale()[0] or "en_US"
            lang = system_locale if system_locale in ["pt_BR", "en_US"] else "en_US"
        _current_lang = lang
        for l in ["en_US", "pt_BR"]:
            _TRANSLATIONS[l] = _load_lang(l)

    def t(key: str, lang: str | None = None) -> str:
        """Traduz uma chave. Fallback para en_US se não encontrada."""
        target = lang or _current_lang
        translation = _TRANSLATIONS.get(target, {}).get(key)
        if translation is None:
            translation = _TRANSLATIONS.get("en_US", {}).get(key, key)
        return translation
    ```

    Em `src/i18n/pt_BR.json`:
    ```json
    {
      "app.title": "SysBoost — Otimizador de Sistema",
      "app.loading": "Carregando...",
      "app.detecting": "Detectando hardware...",
      "nav.overview": "Visão Geral",
      "nav.monitor": "Monitor",
      "nav.optimize": "Otimizar",
      "nav.benchmark": "Benchmark",
      "nav.history": "Histórico",
      "nav.plugins": "Plugins",
      "score.label": "Score de Saúde",
      "optimize.apply_all": "Aplicar Todas",
      "optimize.revert_all": "Reverter Todas",
      "status.applied": "Aplicada",
      "status.pending": "Pendente",
      "status.incompatible": "Incompatível"
    }
    ```

    Em `src/i18n/en_US.json`:
    ```json
    {
      "app.title": "SysBoost — System Optimizer",
      "app.loading": "Loading...",
      "app.detecting": "Detecting hardware...",
      "nav.overview": "Overview",
      "nav.monitor": "Monitor",
      "nav.optimize": "Optimize",
      "nav.benchmark": "Benchmark",
      "nav.history": "History",
      "nav.plugins": "Plugins",
      "score.label": "Health Score",
      "optimize.apply_all": "Apply All",
      "optimize.revert_all": "Revert All",
      "status.applied": "Applied",
      "status.pending": "Pending",
      "status.incompatible": "Incompatible"
    }
    ```
  </action>
  <acceptance_criteria>
    - `src/i18n/__init__.py` contém `def t(key: str`
    - `src/i18n/__init__.py` contém `def init(lang:`
    - `src/i18n/pt_BR.json` é JSON válido e contém `"nav.overview": "Visão Geral"`
    - `src/i18n/en_US.json` é JSON válido e contém `"nav.overview": "Overview"`
    - Executar `python -c "from src.i18n import init, t; init('pt_BR'); print(t('nav.overview'))"` retorna `Visão Geral`
  </acceptance_criteria>
</task>
```

## Verificação da Fase

```bash
# Verificar estrutura completa
python -c "from src.plugins.base import SysBoostPlugin; from src.i18n import init, t; init('pt_BR'); print('Estrutura OK')"

# Verificar versão
python -c "import src; print(src.__version__)"
# Esperado: 0.1.0
```

## Must-Haves

- [ ] Estrutura de diretórios completa criada
- [ ] `src/plugins/base.py` com interface `SysBoostPlugin` e `OptimizationResult`
- [ ] Sistema de i18n funcional com pt-BR e en-US
- [ ] Plugin de exemplo implementado
- [ ] `.gitignore` configurado
