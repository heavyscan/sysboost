---
id: "4.7"
phase: 4
wave: 3
title: "Sistema de Revert para Windows"
depends_on: ["4.1", "4.2", "4.3", "4.4", "4.5", "4.6"]
files_modified:
  - "src/core/revert.py"
autonomous: true
requirements:
  - RF-07
---

# Plano 4.7 — Sistema de Revert (Windows)

## Objetivo

Implementar a lógica de reversão para todas as otimizações aplicadas no Windows, garantindo que o sistema possa retornar ao estado original.

## Tarefas

### Task 1 — Implementar Reversão Global

```xml
<task id="4.7.1">
  <title>Criar lógica de rollback no revert.py</title>
  <read_first>
    - src/core/revert.py
    - src/core/optimizer.py
  </read_first>
  <action>
    Atualizar `src/core/revert.py`:
    - Adicionar método `revert_optimization(record_id)`.
    - Implementar handlers específicos para cada tipo de otimização (Registry, Service, PowerCfg).
  </action>
  <acceptance_criteria>
    - Otimizações são desfeitas corretamente e o registro é atualizado para status "Reverted".
  </acceptance_criteria>
</task>
```
