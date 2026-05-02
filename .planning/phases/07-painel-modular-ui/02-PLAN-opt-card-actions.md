---
id: "7.2"
phase: 7
wave: 1
title: "Componente OptimizationCard e Ações"
depends_on: ["7.1"]
files_modified:
  - "src/ui/components/opt_card.py"
  - "src/ui/frames/optimize.py"
autonomous: true
requirements:
  - RF-07
---

# Plano 7.2 — OptimizationCard e Ações

## Objetivo

Criar um componente reutilizável para representar cada otimização, com descrição e botão de ação (Aplicar/Reverter).

## Tarefas

### Task 1 — Criar Componente OptimizationCard

```xml
<task id="7.2.1">
  <title>Implementar componente visual de card</title>
  <action>
    Criar `src/ui/components/opt_card.py`:
    - Classe `OptimizationCard`.
    - Exibir: Título, Descrição, Badge de Categoria.
    - Botão de ação dinâmico (texto muda conforme status).
  </action>
  <acceptance_criteria>
    - Card exibe informações corretamente.
  </acceptance_criteria>
</task>
```

### Task 2 — Implementar Lógica de Clique

```xml
<task id="7.2.2">
  <title>Conectar botões às ações do optimizer</title>
  <read_first>
    - src/core/optimizer.py
  </read_first>
  <action>
    No `OptimizeFrame`, passar callbacks para cada card:
    - Ao clicar em "Aplicar", chamar o método correspondente no Optimizer.
    - Atualizar o status do card após a execução.
  </action>
  <acceptance_criteria>
    - Clique no botão dispara a otimização no core.
  </acceptance_criteria>
</task>
```
