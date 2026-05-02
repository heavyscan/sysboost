---
id: "3.1"
phase: 3
wave: 1
title: "Layout principal: sidebar de navegação e barra de status"
depends_on: []
files_modified:
  - "src/ui/app.py"
  - "src/ui/navigation.py"
autonomous: true
requirements:
  - RF-08
---

# Plano 3.1 — Layout Principal

## Objetivo

Implementar a estrutura base da interface do SysBoost, utilizando um padrão moderno de sidebar lateral para navegação e uma área central para os frames de conteúdo (Overview, Monitor, Otimizações, etc.).

## Tarefas

### Task 1 — Criar Sidebar e Sistema de Navegação

```xml
<task id="3.1.1">
  <title>Implementar Sidebar e navegação entre frames</title>
  <read_first>
    - src/ui/app.py
    - src/i18n/en_US.json (para as labels de navegação)
  </read_first>
  <action>
    Criar a estrutura de navegação em `src/ui/app.py` substituindo o placeholder:
    - Adicionar um frame lateral (`sidebar_frame`) com logo e botões.
    - Criar um sistema para alternar entre frames de conteúdo.
    - Adicionar uma barra de status inferior.
  </action>
  <acceptance_criteria>
    - Sidebar lateral visível com botões "Overview", "Monitor", "Optimize".
    - Área de conteúdo central que muda conforme o botão pressionado.
    - Barra de status na parte inferior exibindo o estado do sistema.
  </acceptance_criteria>
</task>
```
