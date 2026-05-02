---
id: "6.4"
phase: 6
wave: 2
title: "Limpeza de Caches macOS"
depends_on: []
files_modified:
  - "src/core/optimizer.py"
autonomous: true
requirements:
  - RF-06
---

# Plano 6.4 — Limpeza de Caches (macOS)

## Objetivo

Remover arquivos temporários e caches de sistema/usuário que podem estar corrompidos ou ocupando espaço excessivo, forçando o sistema a reconstruí-los.

## Tarefas

### Task 1 — Implementar Limpeza de Pastas Library

```xml
<task id="6.4.1">
  <title>Criar rotinas de limpeza de cache</title>
  <read_first>
    - src/core/optimizer.py
  </read_first>
  <action>
    Adicionar método `clear_macos_caches()`:
    - Limpar `~/Library/Caches/*`.
    - Limpar `/Library/Caches/*`.
    - Limpar `/private/var/folders/*` (requer cuidado e root).
  </action>
  <acceptance_criteria>
    - Arquivos removidos e espaço liberado reportado.
  </acceptance_criteria>
</task>
```
