---
id: "3.5"
phase: 3
wave: 1
title: "Threading: worker em background para coleta de métricas"
depends_on: ["3.1"]
files_modified:
  - "src/ui/app.py"
  - "src/core/worker.py"
autonomous: true
requirements:
  - RNF-02
---

# Plano 3.5 — Threading e Background Worker

## Objetivo

Implementar um sistema de threading para que a coleta de dados (detector, monitor, benchmarks) ocorra em segundo plano, garantindo que a interface do usuário (UI) permaneça fluida e responsiva (60 FPS).

## Tarefas

### Task 1 — Implementar Background Worker

```xml
<task id="3.5.1">
  <title>Criar o worker de background para atualização da UI</title>
  <read_first>
    - src/ui/app.py
  </read_first>
  <action>
    Criar `src/core/worker.py` (ou integrar em `app.py`):
    - Implementar uma thread dedicada para loop de coleta (1s).
    - Usar `queue` ou `after()` do CustomTkinter para enviar dados de volta para a thread principal da UI.
    - Garantir o encerramento limpo da thread ao fechar o app.
  </action>
  <acceptance_criteria>
    - App não "trava" enquanto detecta hardware ou coleta métricas.
    - Uso de CPU do monitoramento dentro do limite de 2% (RNF-02).
  </acceptance_criteria>
</task>
```
