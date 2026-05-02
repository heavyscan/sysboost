---
id: "7.1"
phase: 7
wave: 1
title: "Frame de Otimizações: Listagem Dinâmica"
depends_on: []
files_modified:
  - "src/ui/frames/optimize.py"
  - "src/ui/app.py"
autonomous: true
requirements:
  - RF-07
  - RF-08
---

# Plano 7.1 — Frame de Otimizações

## Objetivo

Criar a estrutura base da tela de otimizações, que exibirá cards dinâmicos baseados no sistema operacional detectado.

## Tarefas

### Task 1 — Criar OptimizeFrame

```xml
<task id="7.1.1">
  <title>Implementar base do OptimizeFrame</title>
  <read_first>
    - src/ui/frames/overview.py (para padrão de design)
  </read_first>
  <action>
    Criar `src/ui/frames/optimize.py`:
    - Implementar classe `OptimizeFrame`.
    - Adicionar um `ctk.CTkScrollableFrame` para conter a lista de otimizações.
    - Criar método `_load_optimizations()` que decide quais otimizações mostrar (Win/Lin/Mac).
  </action>
  <acceptance_criteria>
    - Tela de otimização carregada no app.
  </acceptance_criteria>
</task>
```

### Task 2 — Integrar no App

```xml
<task id="7.1.2">
  <title>Registrar OptimizeFrame no app.py</title>
  <read_first>
    - src/ui/app.py
  </read_first>
  <action>
    Atualizar `src/ui/app.py`:
    - Importar `OptimizeFrame`.
    - Substituir o placeholder por uma instância real.
  </action>
  <acceptance_criteria>
    - Navegação para "Optimize" funciona e mostra o novo frame.
  </acceptance_criteria>
</task>
```
