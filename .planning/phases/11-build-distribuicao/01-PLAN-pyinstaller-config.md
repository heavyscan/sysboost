---
id: "11.1"
phase: 11
wave: 1
title: "Configuração do PyInstaller (Spec File)"
depends_on: []
files_modified:
  - "sysboost.spec"
autonomous: true
requirements:
  - RF-11
---

# Plano 11.1 — Configuração de Build

## Objetivo

Configurar o arquivo `.spec` do PyInstaller para garantir que todos os recursos (JSONs de tradução, imagens, arquivos temporários) sejam incluídos corretamente no executável final.

## Tarefas

### Task 1 — Criar sysboost.spec

```xml
<task id="11.1.1">
  <title>Definir recursos e dependências no spec</title>
  <action>
    Criar `sysboost.spec`:
    - Adicionar `datas=[('src/i18n/locales/*.json', 'src/i18n/locales')]`.
    - Configurar como `onefile` (opcional, dependendo do tamanho).
    - Definir `noconsole=True` para evitar janelas de terminal.
  </action>
  <acceptance_criteria>
    - Arquivo .spec gerado e configurado para incluir ativos.
  </acceptance_criteria>
</task>
```
