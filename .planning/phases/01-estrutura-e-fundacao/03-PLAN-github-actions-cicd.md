---
id: "1.3"
phase: 1
wave: 2
title: "Configurar GitHub Actions: CI/CD completo"
depends_on: ["1.2"]
files_modified:
  - ".github/workflows/ci.yml"
  - ".github/workflows/release.yml"
  - ".github/ISSUE_TEMPLATE/bug_report.md"
  - ".github/ISSUE_TEMPLATE/feature_request.md"
  - ".github/pull_request_template.md"
  - "build/windows.spec"
  - "build/linux.spec"
  - "build/macos.spec"
autonomous: true
requirements:
  - RF-10
  - RNF-03
---

# Plano 1.3 — Configurar GitHub Actions: CI/CD Completo

## Objetivo

Criar pipeline CI/CD no GitHub Actions com: lint automático (ruff), testes (pytest) nos 3 OSes, e build de executáveis (PyInstaller) disparado por tags de release. Incluir templates de issue e PR para padronizar contribuições.

## Tarefas

### Task 1 — Workflow de CI (lint + testes)

```xml
<task id="1.3.1">
  <title>Criar workflow ci.yml para lint e testes automáticos</title>
  <read_first>
    - pyproject.toml (configurações de pytest e ruff)
    - F:\Automações\customização\.planning\REQUIREMENTS.md (RNF-03: Compatibilidade de OS)
  </read_first>
  <action>
    Criar `.github/workflows/ci.yml`:

    ```yaml
    name: CI

    on:
      push:
        branches: [main, develop]
      pull_request:
        branches: [main]

    jobs:
      lint:
        name: Lint (ruff)
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v4
          - uses: actions/setup-python@v5
            with:
              python-version: "3.11"
          - name: Install ruff
            run: pip install ruff
          - name: Run ruff check
            run: ruff check src/ tests/
          - name: Run ruff format check
            run: ruff format --check src/ tests/

      test:
        name: Tests (${{ matrix.os }})
        needs: lint
        runs-on: ${{ matrix.os }}
        strategy:
          fail-fast: false
          matrix:
            os: [ubuntu-latest, windows-latest, macos-latest]
            python-version: ["3.11", "3.12"]
        steps:
          - uses: actions/checkout@v4
          - uses: actions/setup-python@v5
            with:
              python-version: ${{ matrix.python-version }}
          - name: Install dependencies
            run: pip install -r requirements-dev.txt
          - name: Install package
            run: pip install -e .
          - name: Run tests
            run: pytest tests/unit/ -v --tb=short
            env:
              SYSBOOST_TEST_MODE: "1"
    ```
  </action>
  <acceptance_criteria>
    - `.github/workflows/ci.yml` existe
    - Arquivo contém `runs-on: ${{ matrix.os }}`
    - Arquivo contém `ubuntu-latest, windows-latest, macos-latest`
    - Arquivo contém `ruff check src/`
    - Arquivo contém `python-version: "3.11"`
    - YAML é válido (sem erros de indentação)
  </acceptance_criteria>
</task>
```

### Task 2 — Workflow de Release (build de executáveis)

```xml
<task id="1.3.2">
  <title>Criar workflow release.yml para build de executáveis</title>
  <read_first>
    - .github/workflows/ci.yml (após Task 1.3.1)
    - pyproject.toml (versão e metadados)
  </read_first>
  <action>
    Criar `.github/workflows/release.yml`:

    ```yaml
    name: Release

    on:
      push:
        tags:
          - "v*.*.*"

    permissions:
      contents: write

    jobs:
      build-windows:
        name: Build Windows (.exe)
        runs-on: windows-latest
        steps:
          - uses: actions/checkout@v4
          - uses: actions/setup-python@v5
            with:
              python-version: "3.11"
          - name: Install dependencies
            run: pip install -r requirements-dev.txt && pip install -e .
          - name: Build executable
            run: pyinstaller build/windows.spec
          - name: Upload artifact
            uses: actions/upload-artifact@v4
            with:
              name: SysBoost-Windows
              path: dist/SysBoost.exe

      build-linux:
        name: Build Linux (AppImage)
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v4
          - uses: actions/setup-python@v5
            with:
              python-version: "3.11"
          - name: Install system deps
            run: sudo apt-get install -y python3-tk tk-dev
          - name: Install dependencies
            run: pip install -r requirements-dev.txt && pip install -e .
          - name: Build executable
            run: pyinstaller build/linux.spec
          - name: Upload artifact
            uses: actions/upload-artifact@v4
            with:
              name: SysBoost-Linux
              path: dist/SysBoost

      build-macos:
        name: Build macOS (.app)
        runs-on: macos-latest
        steps:
          - uses: actions/checkout@v4
          - uses: actions/setup-python@v5
            with:
              python-version: "3.11"
          - name: Install dependencies
            run: pip install -r requirements-dev.txt && pip install -e .
          - name: Build executable
            run: pyinstaller build/macos.spec
          - name: Upload artifact
            uses: actions/upload-artifact@v4
            with:
              name: SysBoost-macOS
              path: dist/SysBoost.app

      create-release:
        name: Create GitHub Release
        needs: [build-windows, build-linux, build-macos]
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v4
          - name: Download all artifacts
            uses: actions/download-artifact@v4
          - name: Create Release
            uses: softprops/action-gh-release@v1
            with:
              files: |
                SysBoost-Windows/SysBoost.exe
                SysBoost-Linux/SysBoost
                SysBoost-macOS/SysBoost.app
              generate_release_notes: true
    ```

    Criar `build/windows.spec` (PyInstaller spec para Windows):
    ```python
    # -*- mode: python ; coding: utf-8 -*-
    block_cipher = None

    a = Analysis(
        ['src/ui/app.py'],
        pathex=[],
        binaries=[],
        datas=[
            ('src/i18n/*.json', 'src/i18n'),
        ],
        hiddenimports=['customtkinter', 'psutil', 'PIL'],
        hookspath=[],
        cipher=block_cipher,
    )
    pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
    exe = EXE(
        pyz, a.scripts, a.binaries, a.zipfiles, a.datas,
        name='SysBoost',
        debug=False,
        console=False,
        icon='docs/assets/icon.ico',
    )
    ```

    Criar `build/linux.spec` e `build/macos.spec` com conteúdo idêntico ao windows.spec exceto:
    - linux.spec: remover `icon=`, alterar `console=True`
    - macos.spec: usar `BUNDLE` em vez de `EXE` com `bundle_identifier='com.sysboost.app'`
  </action>
  <acceptance_criteria>
    - `.github/workflows/release.yml` existe
    - Arquivo contém `on: push: tags: - "v*.*.*"`
    - Arquivo contém `build-windows:`, `build-linux:`, `build-macos:`
    - Arquivo contém `create-release:`
    - `build/windows.spec` existe e contém `Analysis(`
    - `build/linux.spec` existe
    - `build/macos.spec` existe
  </acceptance_criteria>
</task>
```

### Task 3 — Templates de Issue e PR

```xml
<task id="1.3.3">
  <title>Criar templates de Issue e Pull Request</title>
  <read_first>
    - F:\Automações\customização\.planning\PROJECT.md (público-alvo e escopo)
  </read_first>
  <action>
    Criar `.github/ISSUE_TEMPLATE/bug_report.md`:
    ```markdown
    ---
    name: Bug Report
    about: Reportar um problema com o SysBoost
    labels: bug
    ---

    ## Descrição do Bug
    <!-- Descreva o problema de forma clara e concisa -->

    ## Passos para Reproduzir
    1. ...
    2. ...

    ## Comportamento Esperado
    <!-- O que deveria acontecer -->

    ## Comportamento Atual
    <!-- O que está acontecendo -->

    ## Ambiente
    - OS: [ex: Windows 11, Ubuntu 22.04, macOS 13]
    - SysBoost versão: [ex: 0.1.0]
    - Python versão: [ex: 3.11.5] (se rodando do código-fonte)

    ## Screenshots / Logs
    <!-- Anexe screenshots ou logs de erro se relevante -->
    ```

    Criar `.github/ISSUE_TEMPLATE/feature_request.md`:
    ```markdown
    ---
    name: Feature Request
    about: Sugerir uma nova funcionalidade para o SysBoost
    labels: enhancement
    ---

    ## Problema que a Feature Resolve
    <!-- Ex: Quando faço X, não consigo Y -->

    ## Solução Proposta
    <!-- Descreva o que você gostaria que acontecesse -->

    ## Alternativas Consideradas
    <!-- Outras abordagens que você considerou -->

    ## Contexto Adicional
    <!-- OS alvo, casos de uso específicos, etc. -->
    ```

    Criar `.github/pull_request_template.md`:
    ```markdown
    ## Descrição
    <!-- Descreva as mudanças deste PR -->

    ## Tipo de Mudança
    - [ ] Bug fix
    - [ ] Nova funcionalidade
    - [ ] Refatoração
    - [ ] Documentação
    - [ ] Otimização

    ## Checklist
    - [ ] Testes adicionados/atualizados
    - [ ] `ruff check` passa sem erros
    - [ ] Documentação atualizada (se necessário)
    - [ ] Testado em: [ ] Windows [ ] Linux [ ] macOS
    - [ ] Otimização é reversível (se aplicável)

    ## Screenshots (se mudança de UI)
    <!-- Adicione screenshots antes/depois se relevante -->
    ```
  </action>
  <acceptance_criteria>
    - `.github/ISSUE_TEMPLATE/bug_report.md` existe e contém `name: Bug Report`
    - `.github/ISSUE_TEMPLATE/feature_request.md` existe e contém `name: Feature Request`
    - `.github/pull_request_template.md` existe e contém `- [ ] Testes adicionados`
  </acceptance_criteria>
</task>
```

## Must-Haves

- [ ] `.github/workflows/ci.yml` com lint + testes nos 3 OSes
- [ ] `.github/workflows/release.yml` com build para Windows, Linux e macOS
- [ ] Specs do PyInstaller para os 3 OSes
- [ ] Templates de issue e PR criados
