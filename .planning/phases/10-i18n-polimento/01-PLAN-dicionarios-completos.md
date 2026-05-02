---
id: "10.1"
phase: 10
wave: 1
title: "Dicionários Completos (i18n)"
depends_on: []
files_modified:
  - "src/i18n/locales/en.json"
  - "src/i18n/locales/pt.json"
autonomous: true
requirements:
  - RF-10
---

# Plano 10.1 — Dicionários i18n

## Objetivo

Completar as traduções para todos os textos da interface do SysBoost, garantindo que o app suporte plenamente Português e Inglês.

## Tarefas

### Task 1 — Atualizar locales/en.json

```xml
<task id="10.1.1">
  <title>Preencher dicionário de Inglês</title>
  <action>
    Atualizar `src/i18n/locales/en.json`:
    - Adicionar chaves para Overview, Monitor, Optimize, History, Benchmark, Plugins e Settings.
  </action>
  <acceptance_criteria>
    - Todas as chaves utilizadas no código possuem tradução em EN.
  </acceptance_criteria>
</task>
```

### Task 2 — Atualizar locales/pt.json

```xml
<task id="10.1.2">
  <title>Preencher dicionário de Português</title>
  <action>
    Atualizar `src/i18n/locales/pt.json`:
    - Adicionar chaves correspondentes ao JSON de inglês.
  </action>
  <acceptance_criteria>
    - Todas as chaves utilizadas no código possuem tradução em PT.
  </acceptance_criteria>
</task>
```
