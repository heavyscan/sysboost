---
id: "5.3"
phase: 5
wave: 1
title: "Otimização de I/O Scheduler"
depends_on: []
files_modified:
  - "src/core/optimizer.py"
autonomous: true
requirements:
  - RF-05
---

# Plano 5.3 — I/O Scheduler (Linux)

## Objetivo

Otimizar o escalonador de entrada/saída de disco baseado no tipo de drive (SSD vs HDD) para reduzir latência e aumentar throughput.

## Tarefas

### Task 1 — Implementar Tuning de Scheduler

```xml
<task id="5.3.1">
  <title>Ajustar escalonadores de disco</title>
  <read_first>
    - src/core/detector.py (para identificar tipo de disco)
  </read_first>
  <action>
    Adicionar método `optimize_linux_disk_scheduler()`:
    - Identificar discos em `/sys/block/*/queue/scheduler`.
    - Se SSD/NVMe: definir para `mq-deadline` ou `none`.
    - Se HDD: definir para `bfq`.
    - Aplicar via `echo` direcionado para o arquivo de sistema do scheduler.
  </action>
  <acceptance_criteria>
    - Scheduler alterado conforme o tipo de hardware detectado.
  </acceptance_criteria>
</task>
```
