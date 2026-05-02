---
id: "5.2"
phase: 5
wave: 1
title: "Tuning de Swappiness e VFS Cache Pressure"
depends_on: []
files_modified:
  - "src/core/optimizer.py"
autonomous: true
requirements:
  - RF-05
---

# Plano 5.2 — Swappiness e VFS Cache

## Objetivo

Otimizar o uso de memória virtual e cache de arquivos no Linux através dos parâmetros `vm.swappiness` e `vm.vfs_cache_pressure` no sysctl.

## Tarefas

### Task 1 — Tuning de Memória Virtual via Sysctl

```xml
<task id="5.2.1">
  <title>Implementar ajuste de swappiness e cache pressure</title>
  <read_first>
    - src/core/optimizer.py
    - src/core/detector.py (para verificar RAM total)
  </read_first>
  <action>
    Adicionar método `optimize_linux_memory_params()`:
    - Se RAM >= 8GB: definir `vm.swappiness=10`.
    - Se RAM < 8GB: definir `vm.swappiness=30`.
    - Definir `vm.vfs_cache_pressure=50` (valor mais agressivo para manter cache).
    - Usar comando `sysctl -w`.
  </action>
  <acceptance_criteria>
    - Valores alterados em tempo de execução via sysctl.
  </acceptance_criteria>
</task>
```
