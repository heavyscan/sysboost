---
id: "5.7"
phase: 5
wave: 3
title: "Sistema de Revert para Linux"
depends_on: ["5.1", "5.2", "5.3", "5.4", "5.5", "5.6"]
files_modified:
  - "src/core/revert.py"
autonomous: true
requirements:
  - RF-07
---

# Plano 5.7 — Sistema de Revert (Linux)

## Objetivo

Implementar a lógica de reversão para todas as otimizações aplicadas no Linux, restaurando os valores originais do sysctl, governors e serviços.

## Tarefas

### Task 1 — Implementar Rollback Linux

```xml
<task id="5.7.1">
  <title>Adicionar handlers de reversão Linux no revert.py</title>
  <read_first>
    - src/core/revert.py
  </read_first>
  <action>
    Atualizar `src/core/revert.py`:
    - Adicionar suporte para `lin_cpu_governor`, `lin_sysctl`, `lin_svc`.
    - Garantir que as mudanças temporárias (sysctl -w) e persistentes (/etc/sysctl.conf) sejam tratadas.
  </action>
  <acceptance_criteria>
    - Otimizações Linux revertidas com sucesso no histórico.
  </acceptance_criteria>
</task>
```
