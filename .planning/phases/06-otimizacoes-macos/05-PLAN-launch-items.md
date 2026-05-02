---
id: "6.5"
phase: 6
wave: 3
title: "Gestor de LaunchAgents e LaunchDaemons"
depends_on: []
files_modified:
  - "src/core/optimizer.py"
autonomous: true
requirements:
  - RF-06
---

# Plano 6.5 — LaunchAgents (macOS)

## Objetivo

Auditar e gerenciar itens de inicialização do macOS localizados em `LaunchAgents` e `LaunchDaemons`, permitindo desativar serviços de terceiros que impactam o boot.

## Tarefas

### Task 1 — Auditoria de LaunchItems

```xml
<task id="6.5.1">
  <title>Listar e gerenciar itens de boot macOS</title>
  <read_first>
    - src/core/optimizer.py
  </read_first>
  <action>
    Adicionar métodos no `MacOSOptimizer`:
    - `list_launch_items()`: Listar `.plist` em `/Library/LaunchAgents`, `/Library/LaunchDaemons` e `~/Library/LaunchAgents`.
    - `disable_launch_item(label)`: Executar `launchctl unload -w <path>`.
  </action>
  <acceptance_criteria>
    - Itens listados com sucesso na UI/Log.
  </acceptance_criteria>
</task>
```
