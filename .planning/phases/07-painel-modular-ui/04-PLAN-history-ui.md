---
id: "7.4"
phase: 7
wave: 2
title: "Aba de Histórico e Reversão"
depends_on: ["7.1"]
files_modified:
  - "src/ui/frames/history.py"
  - "src/ui/app.py"
autonomous: true
requirements:
  - RF-07
---

# Plano 7.4 — Aba de Histórico

## Objetivo

Implementar a tela de histórico onde o usuário pode ver uma lista cronológica de todas as otimizações aplicadas e reverter qualquer uma delas individualmente.

## Tarefas

### Task 1 — Criar HistoryFrame

```xml
<task id="7.4.1">
  <title>Implementar tela de log histórico</title>
  <read_first>
    - src/core/revert.py (HistoryManager)
  </read_first>
  <action>
    Criar `src/ui/frames/history.py`:
    - Listar itens do `history.json` em uma tabela ou lista de cards compactos.
    - Botão "Rollback" para cada item que chama `revert_optimization()`.
  </action>
  <acceptance_criteria>
    - Histórico carregado corretamente e reversão funcional pela UI.
  </acceptance_criteria>
</task>
```
