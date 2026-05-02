---
id: "7.3"
phase: 7
wave: 2
title: "Feedback Visual e Status"
depends_on: ["7.2"]
files_modified:
  - "src/ui/frames/optimize.py"
autonomous: true
requirements:
  - RF-08
---

# Plano 7.3 — Feedback Visual (Status)

## Objetivo

Melhorar a experiência do usuário indicando claramente quais otimizações já estão aplicadas, quais falharam e o progresso das ações.

## Tarefas

### Task 1 — Implementar Badges de Status

```xml
<task id="7.3.1">
  <title>Adicionar cores e ícones de status</title>
  <action>
    Atualizar `OptimizationCard`:
    - Adicionar um pequeno indicador de cor: Verde (Aplicado), Cinza (Pendente), Vermelho (Erro).
    - Adicionar animação de carregamento (opcional ou texto "Applying...") durante a execução.
  </action>
  <acceptance_criteria>
    - Status visual reflete o estado real da otimização.
  </acceptance_criteria>
</task>
```
