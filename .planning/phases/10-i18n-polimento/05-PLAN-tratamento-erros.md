---
id: "10.5"
phase: 10
wave: 3
title: "Tratamento de Erros Global e Logs"
depends_on: []
files_modified:
  - "src/core/logger.py"
  - "src/ui/app.py"
autonomous: true
requirements:
  - RF-01
---

# Plano 10.5 — Tratamento de Erros e Logs

## Objetivo

Garantir que qualquer falha inesperada seja capturada, logada e apresentada ao usuário de forma amigável, evitando que o app feche abruptamente.

## Tarefas

### Task 1 — Implementar Global Exception Handler

```xml
<task id="10.5.1">
  <title>Capturar erros não tratados na UI</title>
  <action>
    - Adicionar um wrapper no loop principal do CustomTkinter para capturar exceções.
    - Logar o stack trace completo no diretório de logs.
    - Mostrar um Toast de erro genérico ao usuário.
  </action>
  <acceptance_criteria>
    - Exceções críticas não causam crash silencioso do app.
  </acceptance_criteria>
</task>
```
