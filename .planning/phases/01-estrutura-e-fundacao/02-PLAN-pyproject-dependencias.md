---
id: "1.2"
phase: 1
wave: 1
title: "Configurar pyproject.toml, dependências e ambiente virtual"
depends_on: ["1.1"]
files_modified:
  - "pyproject.toml"
  - "requirements.txt"
  - "requirements-dev.txt"
  - ".python-version"
autonomous: true
requirements:
  - RNF-03
---

# Plano 1.2 — Configurar pyproject.toml, Dependências e Ambiente Virtual

## Objetivo

Configurar o projeto Python com `pyproject.toml` completo (metadados, dependências, ferramentas de lint e build), arquivos de requirements separados por ambiente, e documentar como criar o virtualenv.

## Contexto

**Python mínimo:** 3.11 (necessário para `str | None` syntax, `tomllib` built-in)
**Gerenciador de build:** `hatchling` (moderno, suporte nativo a `pyproject.toml`)
**Lint:** `ruff` (substitui flake8 + isort + black, muito mais rápido)
**Testes:** `pytest` + `pytest-cov`
**Build executável:** `pyinstaller`

## Tarefas

### Task 1 — Criar pyproject.toml completo

```xml
<task id="1.2.1">
  <title>Criar pyproject.toml com metadados e dependências</title>
  <read_first>
    - F:\Automações\customização\.planning\PROJECT.md
    - F:\Automações\customização\.planning\REQUIREMENTS.md (RNF-03: Compatibilidade)
  </read_first>
  <action>
    Criar `pyproject.toml` na raiz do projeto com o conteúdo exato abaixo:

    ```toml
    [build-system]
    requires = ["hatchling"]
    build-backend = "hatchling.build"

    [project]
    name = "sysboost"
    version = "0.1.0"
    description = "Cross-platform system performance optimizer with visual dashboard"
    readme = "README.md"
    license = { file = "LICENSE" }
    authors = [{ name = "SysBoost Contributors" }]
    keywords = ["performance", "optimizer", "system", "tuning", "cross-platform"]
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Desktop Environment",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities",
    ]
    requires-python = ">=3.11"
    dependencies = [
        "customtkinter>=5.2.0",
        "psutil>=5.9.0",
        "platformdirs>=4.0.0",
        "pillow>=10.0.0",
    ]

    [project.optional-dependencies]
    dev = [
        "pytest>=7.4.0",
        "pytest-cov>=4.1.0",
        "ruff>=0.1.0",
        "pyinstaller>=6.0.0",
        "pre-commit>=3.5.0",
    ]

    [project.scripts]
    sysboost = "src.ui.app:main"

    [project.urls]
    Homepage = "https://github.com/sysboost/sysboost"
    Repository = "https://github.com/sysboost/sysboost"
    Issues = "https://github.com/sysboost/sysboost/issues"

    [tool.hatch.build.targets.wheel]
    packages = ["src"]

    [tool.ruff]
    target-version = "py311"
    line-length = 100
    select = ["E", "F", "I", "N", "W", "UP", "B", "SIM"]
    ignore = ["E501"]

    [tool.ruff.isort]
    known-first-party = ["src"]

    [tool.pytest.ini_options]
    testpaths = ["tests"]
    python_files = ["test_*.py"]
    python_classes = ["Test*"]
    python_functions = ["test_*"]
    addopts = "--cov=src --cov-report=term-missing --cov-report=html"

    [tool.coverage.run]
    source = ["src"]
    omit = ["tests/*", "plugins/*"]
    ```
  </action>
  <acceptance_criteria>
    - `pyproject.toml` existe na raiz
    - `pyproject.toml` contém `requires-python = ">=3.11"`
    - `pyproject.toml` contém `"customtkinter>=5.2.0"`
    - `pyproject.toml` contém `"psutil>=5.9.0"`
    - `pyproject.toml` contém `[tool.ruff]`
    - `pyproject.toml` contém `[tool.pytest.ini_options]`
    - Executar `python -c "import tomllib; tomllib.loads(open('pyproject.toml').read()); print('TOML válido')"` retorna `TOML válido`
  </acceptance_criteria>
</task>
```

### Task 2 — Criar requirements.txt e requirements-dev.txt

```xml
<task id="1.2.2">
  <title>Criar arquivos de requirements pinados</title>
  <read_first>
    - pyproject.toml (após Task 1.2.1)
  </read_first>
  <action>
    Criar `requirements.txt` (dependências de runtime):
    ```
    customtkinter>=5.2.0
    psutil>=5.9.0
    platformdirs>=4.0.0
    pillow>=10.0.0
    ```

    Criar `requirements-dev.txt` (dependências de desenvolvimento):
    ```
    -r requirements.txt
    pytest>=7.4.0
    pytest-cov>=4.1.0
    ruff>=0.1.0
    pyinstaller>=6.0.0
    pre-commit>=3.5.0
    ```

    Criar `.python-version` com conteúdo:
    ```
    3.11
    ```
  </action>
  <acceptance_criteria>
    - `requirements.txt` contém `customtkinter>=5.2.0`
    - `requirements-dev.txt` contém `-r requirements.txt`
    - `requirements-dev.txt` contém `pytest>=7.4.0`
    - `.python-version` contém `3.11`
  </acceptance_criteria>
</task>
```

### Task 3 — Criar script de setup do ambiente

```xml
<task id="1.2.3">
  <title>Criar scripts de configuração do ambiente de desenvolvimento</title>
  <read_first>
    - requirements-dev.txt (após Task 1.2.2)
  </read_first>
  <action>
    Criar `scripts/setup_dev.py` — script Python cross-platform para configurar o ambiente:

    ```python
    #!/usr/bin/env python3
    """Script de configuração do ambiente de desenvolvimento do SysBoost."""
    import subprocess
    import sys
    from pathlib import Path

    ROOT = Path(__file__).parent.parent

    def run(cmd: list[str], **kwargs) -> int:
        print(f"  $ {' '.join(cmd)}")
        result = subprocess.run(cmd, **kwargs)
        return result.returncode

    def main():
        print("SysBoost — Configurando ambiente de desenvolvimento\n")

        # Criar venv
        print("[1/3] Criando ambiente virtual...")
        if run([sys.executable, "-m", "venv", str(ROOT / ".venv")]) != 0:
            print("ERRO: falha ao criar venv")
            sys.exit(1)

        # Detectar pip no venv
        venv_pip = ROOT / ".venv" / ("Scripts" if sys.platform == "win32" else "bin") / "pip"

        # Instalar dependências de dev
        print("\n[2/3] Instalando dependências...")
        if run([str(venv_pip), "install", "-r", str(ROOT / "requirements-dev.txt")]) != 0:
            print("ERRO: falha ao instalar dependências")
            sys.exit(1)

        # Instalar projeto em modo editável
        print("\n[3/3] Instalando sysboost em modo editável...")
        run([str(venv_pip), "install", "-e", str(ROOT)])

        print("\nAmbiente configurado com sucesso!")
        print("Para ativar: .venv\\Scripts\\activate (Windows) ou source .venv/bin/activate (Linux/macOS)")

    if __name__ == "__main__":
        main()
    ```

    Criar `Makefile` para atalhos de desenvolvimento:
    ```makefile
    .PHONY: setup test lint clean build

    setup:
    	python scripts/setup_dev.py

    test:
    	pytest tests/

    lint:
    	ruff check src/ tests/
    	ruff format --check src/ tests/

    format:
    	ruff format src/ tests/

    clean:
    	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
    	rm -rf build/ dist/ *.egg-info/ .coverage htmlcov/

    build-win:
    	pyinstaller build/windows.spec

    build-linux:
    	pyinstaller build/linux.spec

    build-mac:
    	pyinstaller build/macos.spec
    ```
  </action>
  <acceptance_criteria>
    - `scripts/setup_dev.py` existe
    - `scripts/setup_dev.py` contém `def main():`
    - `scripts/setup_dev.py` contém `subprocess.run`
    - `Makefile` existe
    - `Makefile` contém `test:`
    - `Makefile` contém `lint:`
    - Executar `python scripts/setup_dev.py --help` OU `python -c "import scripts.setup_dev"` não levanta SyntaxError
  </acceptance_criteria>
</task>
```

## Verificação da Fase

```bash
# Verificar TOML
python -c "import tomllib; tomllib.loads(open('pyproject.toml').read()); print('pyproject.toml OK')"

# Verificar requirements
python -c "
import re
req = open('requirements.txt').read()
assert 'customtkinter' in req
assert 'psutil' in req
print('requirements.txt OK')
"
```

## Must-Haves

- [ ] `pyproject.toml` completo e válido com todas as dependências
- [ ] `requirements.txt` e `requirements-dev.txt` criados
- [ ] `.python-version` com `3.11`
- [ ] `scripts/setup_dev.py` funcional
- [ ] `Makefile` com targets: setup, test, lint, clean, build-*
