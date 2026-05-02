---
id: "6.6"
phase: 6
wave: 3
title: "Sistema de Revert para macOS"
depends_on: ["6.1", "6.2", "6.3", "6.4", "6.5"]
files_modified:
  - "src/core/revert.py"
autonomous: true
requirements:
  - RF-07
---

# Plano 6.6 — Sistema de Revert (macOS)

## Objetivo

Implementar a lógica de reversão para todas as otimizações aplicadas no macOS, garantindo que o sistema possa retornar ao estado original.

## Tarefas

### Task 1 — Implementar Rollback macOS

```xml
<task id="6.6.1">
  <title>Adicionar handlers macOS no revert.py</title>
  <read_first>
    - src/core/revert.py
  </read_first>
  <action>
    Atualizar `src/core/revert.py`:
    - Adicionar suporte para `mac_spotlight`, `mac_app_nap`, `mac_launch_item`.
    - Usar `defaults write` e `launchctl load` para restaurar estados.
  </action>
  <acceptance_criteria>
    - Otimizações macOS revertidas com sucesso.
  </acceptance_criteria>
</task>
```
