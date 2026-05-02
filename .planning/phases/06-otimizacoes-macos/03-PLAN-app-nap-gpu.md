---
id: "6.3"
phase: 6
wave: 2
title: "App Nap e Automatic Graphics Switching"
depends_on: []
files_modified:
  - "src/core/optimizer.py"
autonomous: true
requirements:
  - RF-06
---

# Plano 6.3 — App Nap e GPU (macOS)

## Objetivo

Desabilitar o "App Nap" (que pode causar lag em apps de background) e forçar o uso da GPU dedicada (se houver) para evitar engasgos em transições.

## Tarefas

### Task 1 — Tuning de Background e GPU

```xml
<task id="6.3.1">
  <title>Ajustar App Nap e Graphics via defaults/pmset</title>
  <read_first>
    - src/core/optimizer.py
  </read_first>
  <action>
    Adicionar métodos no `MacOSOptimizer`:
    - `disable_app_nap()`: `defaults write NSGlobalDomain NSAppSleepDisabled -bool YES`.
    - `force_dedicated_gpu()`: `sudo pmset -a gpuswitch 1` (em Macs com GPU híbrida).
  </action>
  <acceptance_criteria>
    - Comandos executados e registrados no histórico.
  </acceptance_criteria>
</task>
```
