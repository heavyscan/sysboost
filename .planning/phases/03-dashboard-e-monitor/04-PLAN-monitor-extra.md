---
id: "3.4"
phase: 3
wave: 2
title: "Monitor de Rede e Temperatura"
depends_on: ["3.3"]
files_modified:
  - "src/ui/frames/monitor.py"
  - "src/core/monitor.py"
autonomous: true
requirements:
  - RF-03
---

# Plano 3.4 — Monitor de Rede e Temperatura

## Objetivo

Estender o monitoramento para incluir tráfego de rede (Download/Upload) e temperatura da CPU (onde suportado pelo hardware/OS).

## Tarefas

### Task 1 — Adicionar Rede e Temperatura ao Core

```xml
<task id="3.4.1">
  <title>Adicionar rede e sensores ao MonitorSnapshot</title>
  <read_first>
    - src/core/monitor.py
  </read_first>
  <action>
    Atualizar `src/core/monitor.py`:
    - Adicionar cálculo de KB/s para rede (`psutil.net_io_counters`).
    - Adicionar leitura de temperatura (`psutil.sensors_temperatures`).
    - Garantir que não falhe se os sensores de temperatura não forem acessíveis.
  </action>
  <acceptance_criteria>
    - Snapshot inclui dados de rede e temperatura (ou None se indisponível).
  </acceptance_criteria>
</task>
```

### Task 2 — Atualizar UI com Novos Dados

```xml
<task id="3.4.2">
  <title>Exibir rede e temperatura na UI</title>
  <read_first>
    - src/ui/frames/monitor.py
  </read_first>
  <action>
    Atualizar `src/ui/frames/monitor.py`:
    - Adicionar indicadores de Upload/Download.
    - Adicionar widget de temperatura com mudança de cor (Verde -> Laranja -> Vermelho).
  </action>
  <acceptance_criteria>
    - Dados de rede e temperatura visíveis e atualizados.
  </acceptance_criteria>
</task>
```
