---
id: "11.3"
phase: 11
wave: 2
title: "Script de Build Automatizado"
depends_on: ["11.1", "11.2"]
files_modified:
  - "scripts/build.ps1"
  - "scripts/build.sh"
autonomous: true
requirements:
  - RF-11
---

# Plano 11.3 — Automação de Build

## Objetivo

Criar scripts de automação que realizam a limpeza de builds anteriores, instalam dependências e disparam o PyInstaller com um único comando.

## Tarefas

### Task 1 — Criar Scripts de Build

```xml
<task id="11.3.1">
  <title>Implementar build.ps1 e build.sh</title>
  <action>
    - `scripts/build.ps1` (Windows): Comando para rodar `pyinstaller sysboost.spec`.
    - `scripts/build.sh` (Linux/Mac): Comando equivalente para Unix.
  </action>
  <acceptance_criteria>
    - Script gera o executável na pasta `dist/`.
  </acceptance_criteria>
</task>
```
