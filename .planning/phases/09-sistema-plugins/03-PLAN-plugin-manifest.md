---
id: "9.3"
phase: 9
wave: 2
title: "Sistema de Manifest e Metadados"
depends_on: ["9.2"]
files_modified:
  - "src/plugins/types.py"
autonomous: true
requirements:
  - RF-10
---

# Plano 9.3 — Plugin Manifest

## Objetivo

Definir o formato de metadados (`plugin.json`) que acompanha cada plugin, permitindo exibir informações ricas na UI antes mesmo de carregar o código.

## Tarefas

### Task 1 — Definir Estrutura do Manifest

```xml
<task id="9.3.1">
  <title>Criar validador de plugin.json</title>
  <action>
    - Definir campos obrigatórios: `id`, `name`, `version`, `main_class`, `min_app_version`.
    - Implementar leitura do JSON no `PluginManager`.
  </action>
  <acceptance_criteria>
    - Plugin Manager rejeita plugins sem manifest válido.
  </acceptance_criteria>
</task>
```
