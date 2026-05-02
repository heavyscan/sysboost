---
id: "4.5"
phase: 4
wave: 2
title: "Tuning de Registro: NTFS e Game Mode"
depends_on: ["4.1"]
files_modified:
  - "src/core/optimizer.py"
autonomous: true
requirements:
  - RF-04
---

# Plano 4.5 — Tuning de Registro (Windows)

## Objetivo

Aplicar otimizações avançadas no registro do Windows para melhorar a performance de disco (NTFS) e ativar o modo de jogo (Game Mode).

## Tarefas

### Task 1 — Aplicar Tuning NTFS e Game Mode

```xml
<task id="4.5.1">
  <title>Aplicar chaves de registro para performance</title>
  <read_first>
    - src/core/optimizer.py
  </read_first>
  <action>
    Adicionar chaves no `src/core/optimizer.py`:
    - `NtfsDisable8dot3NameCreation` em `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem`.
    - `GameConfigStore` em `HKEY_CURRENT_USER\Software\Microsoft\GameConfigStore`.
    - `AllowGameDVR` em `HKEY_CURRENT_USER\System\GameConfigStore`.
  </action>
  <acceptance_criteria>
    - Chaves de registro criadas/modificadas.
  </acceptance_criteria>
</task>
```
