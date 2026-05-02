---
id: "6.1"
phase: 6
wave: 1
title: "Monitoramento Térmico e Fans (macOS)"
depends_on: []
files_modified:
  - "src/core/detector.py"
  - "src/core/optimizer.py"
autonomous: true
requirements:
  - RF-06
---

# Plano 6.1 — Thermal e Fans (macOS)

## Objetivo

Implementar o monitoramento de temperatura e controle/alerta de ventoinhas para macOS, essencial para evitar thermal throttling em MacBooks.

## Tarefas

### Task 1 — Implementar Monitoramento Térmico

```xml
<task id="6.1.1">
  <title>Criar suporte a temperatura macOS no detector</title>
  <read_first>
    - src/core/detector.py
  </read_first>
  <action>
    Atualizar `src/core/detector.py`:
    - Adicionar suporte a `osx-cpu-temp` ou comando `powermetrics` (se root) para capturar temperaturas em Apple Silicon e Intel.
  </action>
  <acceptance_criteria>
    - Temperatura da CPU detectada no macOS.
  </acceptance_criteria>
</task>
```

### Task 2 — Lógica de Alerta de Throttling

```xml
<task id="6.1.2">
  <title>Implementar aviso de throttling no macOS</title>
  <read_first>
    - src/core/optimizer.py
  </read_first>
  <action>
    Adicionar classe `MacOSOptimizer` com método `check_thermal_status()`:
    - Usar `pmset -g thermlog` para verificar se o sistema está sofrendo throttling.
    - Registrar no log se o status for crítico.
  </action>
  <acceptance_criteria>
    - Sistema detecta se o macOS está reduzindo clock por calor.
  </acceptance_criteria>
</task>
```
