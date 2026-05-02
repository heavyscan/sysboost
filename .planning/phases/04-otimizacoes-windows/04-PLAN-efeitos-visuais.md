---
id: "4.4"
phase: 4
wave: 2
title: "Otimização de Efeitos Visuais"
depends_on: ["4.1"]
files_modified:
  - "src/core/optimizer.py"
autonomous: true
requirements:
  - RF-04
---

# Plano 4.4 — Efeitos Visuais (Performance)

## Objetivo

Ajustar as configurações visuais do Windows para "Melhor Desempenho", removendo animações e efeitos pesados da interface Aero/DWM.

## Tarefas

### Task 1 — Tuning de Performance Visual

```xml
<task id="4.4.1">
  <title>Implementar ajuste de efeitos visuais via Registro</title>
  <read_first>
    - src/core/optimizer.py
  </read_first>
  <action>
    Adicionar método `optimize_visual_effects()`:
    - Alterar chaves em `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\VisualEffects`.
    - Definir `VisualFXSetting` para 2 (Adjust for best performance).
    - Salvar o valor original para reversão.
  </action>
  <acceptance_criteria>
    - Chave de registro alterada com sucesso.
  </acceptance_criteria>
</task>
```
