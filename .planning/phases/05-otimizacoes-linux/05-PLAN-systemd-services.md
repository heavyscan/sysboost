---
id: "5.5"
phase: 5
wave: 2
title: "Gestor de Serviços Systemd"
depends_on: []
files_modified:
  - "src/core/optimizer.py"
autonomous: true
requirements:
  - RF-05
---

# Plano 5.5 — Systemd Services (Linux)

## Objetivo

Auditar e gerenciar serviços do systemd que iniciam automaticamente, recomendando ou desativando itens não essenciais para reduzir o tempo de boot e consumo de recursos.

## Tarefas

### Task 1 — Auditoria de Serviços

```xml
<task id="5.5.1">
  <title>Listar e analisar serviços systemd</title>
  <read_first>
    - src/core/optimizer.py
  </read_first>
  <action>
    Implementar método `audit_linux_services()`:
    - Executar `systemctl list-unit-files --type=service --state=enabled`.
    - Comparar com uma lista negra de serviços comuns não críticos (ex: bluetooth se não houver adapter, cups se não houver impressora).
    - Oferecer método `disable_linux_service(svc_name)`.
  </action>
  <acceptance_criteria>
    - Lista de serviços habilitados obtida e filtrada.
  </acceptance_criteria>
</task>
```
