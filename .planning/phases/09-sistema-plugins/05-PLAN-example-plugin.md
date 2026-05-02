---
id: "9.5"
phase: 9
wave: 3
title: "Exemplo de Plugin: Custom Cleanup"
depends_on: ["9.1", "9.2"]
files_modified:
  - "plugins/cleanup_plugin/__init__.py"
  - "plugins/cleanup_plugin/plugin.json"
autonomous: true
requirements:
  - RF-10
---

# Plano 9.5 — Exemplo de Plugin

## Objetivo

Criar um plugin de exemplo funcional para demonstrar a arquitetura e permitir que o usuário teste o sistema de extensões imediatamente.

## Tarefas

### Task 1 — Implementar Cleanup Plugin

```xml
<task id="9.5.1">
  <title>Criar plugin de limpeza de arquivos temporários</title>
  <action>
    - Criar estrutura `plugins/cleanup_plugin/`.
    - Implementar logicamente uma limpeza de arquivos `.tmp` em uma pasta específica.
    - Criar o `plugin.json` correspondente.
  </action>
  <acceptance_criteria>
    - Plugin de exemplo carregado e funcional no SysBoost.
  </acceptance_criteria>
</task>
```
