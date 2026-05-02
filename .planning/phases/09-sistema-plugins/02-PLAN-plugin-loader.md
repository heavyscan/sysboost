---
id: "9.2"
phase: 9
wave: 1
title: "Carregador Dinâmico de Plugins"
depends_on: ["9.1"]
files_modified:
  - "src/plugins/manager.py"
autonomous: true
requirements:
  - RF-10
---

# Plano 9.2 — Plugin Loader

## Objetivo

Implementar o motor que descobre e carrega dinamicamente os plugins localizados na pasta `plugins/` do diretório da aplicação.

## Tarefas

### Task 1 — Implementar PluginManager

```xml
<task id="9.2.1">
  <title>Criar PluginManager em src/plugins/manager.py</title>
  <action>
    Criar `src/plugins/manager.py`:
    - Localizar diretório `plugins/`.
    - Usar `importlib` para carregar módulos Python dinamicamente.
    - Instanciar classes que herdam de `BasePlugin`.
    - Gerenciar o ciclo de vida (carregar/descarregar).
  </action>
  <acceptance_criteria>
    - Plugins são detectados e carregados ao iniciar o manager.
  </acceptance_criteria>
</task>
```
