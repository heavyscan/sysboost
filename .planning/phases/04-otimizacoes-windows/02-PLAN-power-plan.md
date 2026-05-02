---
id: "4.2"
phase: 4
wave: 2
title: "Otimização de Power Plan (Windows)"
depends_on: ["4.1"]
files_modified:
  - "src/core/optimizer.py"
autonomous: true
requirements:
  - RF-04
---

# Plano 4.2 — Power Plan (Windows)

## Objetivo

Implementar a otimização de plano de energia para o Windows, permitindo alternar para "High Performance" ou "Ultimate Performance" via comandos `powercfg`.

## Tarefas

### Task 1 — Implementar Otimização de Energia

```xml
<task id="4.2.1">
  <title>Criar script de Power Plan no optimizer.py</title>
  <read_first>
    - src/core/optimizer.py
  </read_first>
  <action>
    Adicionar método `optimize_power_plan()` no `src/core/optimizer.py`:
    - Executar `powercfg /duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61` (High Performance).
    - Executar `powercfg /setactive <GUID>` para ativar.
    - Salvar o GUID anterior para reversão.
  </action>
  <acceptance_criteria>
    - Comando retorna sucesso ou informa se já está ativo.
    - Requer privilégios de administrador.
  </acceptance_criteria>
</task>
```
