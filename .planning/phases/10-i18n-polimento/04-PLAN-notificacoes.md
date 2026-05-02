---
id: "10.4"
phase: 10
wave: 2
title: "Sistema de Notificações Toast"
depends_on: []
files_modified:
  - "src/ui/components/toast.py"
autonomous: true
requirements:
  - RF-08
---

# Plano 10.4 — Sistema de Notificações

## Objetivo

Implementar notificações flutuantes (Toasts) para informar o usuário sobre o sucesso ou falha de ações (ex: "Otimização aplicada com sucesso!") sem interromper o fluxo com popups.

## Tarefas

### Task 1 — Criar Componente Toast

```xml
<task id="10.4.1">
  <title>Implementar sistema de toast notifications</title>
  <action>
    Criar `src/ui/components/toast.py`:
    - Classe `ToastManager`.
    - Pequeno frame que aparece no topo ou base por alguns segundos e desaparece sozinho.
    - Suporte a Success, Warning e Error.
  </action>
  <acceptance_criteria>
    - Notificações visíveis aparecem durante ações de otimização/benchmark.
  </acceptance_criteria>
</task>
```
