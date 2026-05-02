---
id: "11.2"
phase: 11
wave: 1
title: "Ícones e Identidade Visual"
depends_on: []
files_modified:
  - "assets/icon.ico"
  - "assets/icon.png"
autonomous: true
requirements:
  - RF-11
---

# Plano 11.2 — Ícones e Metadados

## Objetivo

Gerar e configurar os ícones do aplicativo e metadados de versão (nome, autor, copyright) para que o executável tenha uma aparência profissional no sistema operacional.

## Tarefas

### Task 1 — Criar Assets de Ícone

```xml
<task id="11.2.1">
  <title>Gerar ícone do SysBoost</title>
  <action>
    - Criar pasta `assets/`.
    - Gerar `icon.png` (512x512).
    - Converter para `icon.ico` (Windows) e `icon.icns` (macOS).
  </action>
  <acceptance_criteria>
    - Arquivos de ícone disponíveis no projeto.
  </acceptance_criteria>
</task>
```
