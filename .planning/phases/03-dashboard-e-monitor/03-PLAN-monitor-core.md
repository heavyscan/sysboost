---
id: "3.3"
phase: 3
wave: 2
title: "Monitor em tempo real: CPU, RAM e Disco"
depends_on: ["3.1"]
files_modified:
  - "src/ui/frames/monitor.py"
  - "src/core/monitor.py"
autonomous: true
requirements:
  - RF-03
---

# Plano 3.3 — Monitor em Tempo Real (Core)

## Objetivo

Implementar a tela de monitoramento com gráficos em tempo real para os recursos fundamentais: uso de CPU por núcleo, uso de RAM e atividade de Disco (I/O).

## Tarefas

### Task 1 — Engine de Coleta de Métricas

```xml
<task id="3.3.1">
  <title>Implementar o módulo core/monitor.py para coleta de snapshots</title>
  <read_first>
    - src/core/types.py (MonitorSnapshot)
  </read_first>
  <action>
    Criar `src/core/monitor.py`:
    - Adicionar método `get_snapshot()` usando `psutil`.
    - Coletar `cpu_percent`, `cpu_count`, `virtual_memory`, `disk_io_counters`.
    - Calcular throughput de disco (bytes lidos/escritos por segundo).
  </action>
  <acceptance_criteria>
    - `src/core/monitor.py` retorna um `MonitorSnapshot` válido.
    - Teste de importação e execução OK.
  </acceptance_criteria>
</task>
```

### Task 2 — UI do Monitor com Gráficos

```xml
<task id="3.3.2">
  <title>Criar a UI de monitoramento com gráficos</title>
  <read_first>
    - src/core/monitor.py
  </read_first>
  <action>
    Criar `src/ui/frames/monitor.py`:
    - Adicionar seção para CPU com barras de progresso ou pequenos gráficos por core.
    - Adicionar gráfico de histórico (últimos 60s) para RAM e Disco.
    - Usar `matplotlib` integrado ou widgets CustomTkinter estilizados.
  </action>
  <acceptance_criteria>
    - Gráficos atualizando visualmente na tela.
    - Layout responsivo que acomoda diferentes números de cores de CPU.
  </acceptance_criteria>
</task>
```
