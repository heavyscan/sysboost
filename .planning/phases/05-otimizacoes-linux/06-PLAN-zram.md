---
id: "5.6"
phase: 5
wave: 3
title: "Configuração de ZRAM"
depends_on: []
files_modified:
  - "src/core/optimizer.py"
autonomous: true
requirements:
  - RF-05
---

# Plano 5.6 — Configuração de ZRAM (Linux)

## Objetivo

Implementar a ativação de ZRAM em sistemas com pouca memória RAM (≤ 8GB) para aumentar a capacidade efetiva de memória através de compressão em tempo real.

## Tarefas

### Task 1 — Ativar e Configurar ZRAM

```xml
<task id="5.6.1">
  <title>Configurar dispositivo zram</title>
  <read_first>
    - src/core/detector.py
  </read_first>
  <action>
    Implementar método `setup_linux_zram()`:
    - Verificar se `zram-tools` ou `zram-config` estão instalados.
    - Se não, configurar via `modprobe zram`.
    - Definir tamanho (ex: 25% da RAM) e algoritmo (zstd ou lzo).
    - Ativar como swap de alta prioridade.
  </action>
  <acceptance_criteria>
    - Dispositivo `/dev/zram0` ativo e listado em `swapon`.
  </acceptance_criteria>
</task>
```
