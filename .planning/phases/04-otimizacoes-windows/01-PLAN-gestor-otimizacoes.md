---
id: "4.1"
phase: 4
wave: 1
title: "Gestor de Otimizações: interface e persistência"
depends_on: []
files_modified:
  - "src/core/optimizer.py"
  - "src/core/revert.py"
autonomous: true
requirements:
  - RF-07
  - RF-08
---

# Plano 4.1 — Gestor de Otimizações

## Objetivo

Implementar a base lógica para gerenciar as otimizações: registro de aplicação, salvamento de estado original para reversão futura e persistência em arquivo.

## Tarefas

### Task 1 — Implementar registro e persistência de histórico

```xml
<task id="4.1.1">
  <title>Criar sistema de persistência para otimizações (history.json)</title>
  <read_first>
    - src/core/types.py (OptimizationRecord)
  </read_first>
  <action>
    Criar `src/core/revert.py`:
    - Implementar `HistoryManager` para salvar/carregar `history.json` no diretório de dados do usuário.
    - Criar métodos `add_record(record)` e `get_history()`.
  </action>
  <acceptance_criteria>
    - Arquivo `history.json` criado e atualizado ao adicionar registros.
  </acceptance_criteria>
</task>
```

### Task 2 — Base do Optimizer

```xml
<task id="4.1.2">
  <title>Adicionar métodos de execução base no optimizer.py</title>
  <read_first>
    - src/core/optimizer.py
  </read_first>
  <action>
    Atualizar `src/core/optimizer.py`:
    - Adicionar método `apply_optimization(opt_id, category)` que registra a ação.
    - Criar um dicionário de status para as otimizações disponíveis.
  </action>
  <acceptance_criteria>
    - Otimizações podem ser "marcadas" como aplicadas no histórico.
  </acceptance_criteria>
</task>
```
