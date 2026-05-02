---
id: "4.6"
phase: 4
wave: 3
title: "Gerenciador de Startup e Pagefile"
depends_on: ["4.1"]
files_modified:
  - "src/core/optimizer.py"
autonomous: true
requirements:
  - RF-04
---

# Plano 4.6 — Startup e Pagefile (Windows)

## Objetivo

Gerenciar os programas que iniciam com o Windows e otimizar o arquivo de paginação (pagefile.sys) para melhor performance em sistemas com pouca ou muita RAM.

## Tarefas

### Task 1 — Tuning de Pagefile

```xml
<task id="4.6.1">
  <title>Implementar configuração automática de Pagefile</title>
  <read_first>
    - src/core/detector.py (para saber a quantidade de RAM)
  </read_first>
  <action>
    Adicionar método `optimize_pagefile()`:
    - Se RAM < 16GB: definir pagefile para 1.5x RAM.
    - Se RAM >= 16GB: definir pagefile fixo de 4096MB para reduzir fragmentação.
    - Usar comandos `wmic` ou registro em `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management`.
  </action>
  <acceptance_criteria>
    - Configuração de memória virtual alterada.
  </acceptance_criteria>
</task>
```
