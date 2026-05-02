---
id: "4.3"
phase: 4
wave: 2
title: "Desabilitar SysMain e Windows Search"
depends_on: ["4.1"]
files_modified:
  - "src/core/optimizer.py"
autonomous: true
requirements:
  - RF-04
---

# Plano 4.3 — SysMain e Windows Search

## Objetivo

Melhorar a performance de disco e responsividade do sistema desabilitando serviços que consomem I/O excessivo (SysMain/Superfetch e Windows Search Indexing).

## Tarefas

### Task 1 — Desabilitar Serviços via SC.exe

```xml
<task id="4.3.1">
  <title>Implementar desativação de serviços desnecessários</title>
  <read_first>
    - src/core/optimizer.py
  </read_first>
  <action>
    Adicionar métodos no `src/core/optimizer.py`:
    - `disable_sysmain()`: Para o serviço `SysMain` e muda startup para disabled.
    - `disable_wsearch()`: Para o serviço `WSearch` e muda startup para disabled.
    - Usar comandos `sc stop` e `sc config start=disabled`.
  </action>
  <acceptance_criteria>
    - Serviços param de rodar e são marcados como desativados no Windows.
  </acceptance_criteria>
</task>
```
