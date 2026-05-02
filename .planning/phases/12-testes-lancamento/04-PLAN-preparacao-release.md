---
id: "12.4"
phase: 12
wave: 2
title: "Preparação de Release v1.0.0"
depends_on: ["11.4", "12.1"]
files_modified: []
autonomous: true
requirements:
  - RF-12
---

# Plano 12.4 — Preparação de Release

## Objetivo

Consolidar todos os binários gerados, documentação e changelog para o lançamento oficial no GitHub.

## Tarefas

### Task 1 — Pack e Upload

```xml
<task id="12.4.1">
  <title>Organizar artefatos de release</title>
  <action>
    - Coletar executáveis compilados (Win/Lin/Mac).
    - Criar tag `v1.0.0` no repositório.
    - Redigir notas de release destacando as principais funcionalidades do MVP.
  </action>
  <acceptance_criteria>
    - Release pronto para publicação.
  </acceptance_criteria>
</task>
```
