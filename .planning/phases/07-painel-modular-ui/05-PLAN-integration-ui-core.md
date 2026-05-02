---
id: "7.5"
phase: 7
wave: 3
title: "Integração Final UI-Core"
depends_on: ["7.2", "7.4"]
files_modified:
  - "src/ui/frames/optimize.py"
  - "src/ui/frames/history.py"
autonomous: true
requirements:
  - RF-07
  - RF-08
---

# Plano 7.5 — Integração Final UI-Core

## Objetivo

Finalizar a conexão entre os componentes visuais e as engines multiplataforma, garantindo que o app se comporte corretamente em Windows, Linux e macOS.

## Tarefas

### Task 1 — Refinar Detecção de OS na UI

```xml
<task id="7.5.1">
  <title>Garantir cards corretos por plataforma</title>
  <action>
    No `OptimizeFrame`, refinar a lógica de carregamento:
    - Usar `platform.system()` para injetar as instâncias corretas de `WindowsOptimizer`, `LinuxOptimizer` ou `MacOSOptimizer`.
  </action>
  <acceptance_criteria>
    - Somente otimizações válidas para o OS atual são exibidas.
  </acceptance_criteria>
</task>
```
