---
id: "6.2"
phase: 6
wave: 1
title: "Otimização de Indexação Spotlight"
depends_on: []
files_modified:
  - "src/core/optimizer.py"
autonomous: true
requirements:
  - RF-06
---

# Plano 6.2 — Spotlight Indexing (macOS)

## Objetivo

Reduzir o consumo de CPU e Disco do processo `mds` desabilitando a indexação em pastas de desenvolvimento ou temporárias, ou desabilitando globalmente se solicitado.

## Tarefas

### Task 1 — Implementar Controle de Spotlight

```xml
<task id="6.2.1">
  <title>Criar métodos para gerenciar mdutil</title>
  <read_first>
    - src/core/optimizer.py
  </read_first>
  <action>
    Adicionar métodos no `MacOSOptimizer`:
    - `disable_spotlight_global()`: Executa `sudo mdutil -a -i off`.
    - `exclude_path_from_spotlight(path)`: Executa `mdutil -i off <path>`.
    - Salvar estado original para reversão.
  </action>
  <acceptance_criteria>
    - Indexação desabilitada conforme comando.
  </acceptance_criteria>
</task>
```
