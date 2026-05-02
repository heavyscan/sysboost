---
id: "3.2"
phase: 3
wave: 1
title: "Tela Overview: score de saúde e cards de hardware"
depends_on: ["3.1"]
files_modified:
  - "src/ui/frames/overview.py"
autonomous: true
requirements:
  - RF-01
  - RF-02
---

# Plano 3.2 — Tela Overview

## Objetivo

Implementar a tela inicial "Overview" que exibe o score de saúde do sistema (gerado pela `ScoreEngine`) e cards informativos com o resumo do hardware detectado (CPU, RAM, Discos, OS).

## Tarefas

### Task 1 — Implementar Frame de Overview

```xml
<task id="3.2.1">
  <title>Criar a tela de Overview com Score e Hardware</title>
  <read_first>
    - src/core/detector.py
    - src/core/optimizer.py
    - src/ui/app.py
  </read_first>
  <action>
    Criar `src/ui/frames/overview.py`:
    - Adicionar um widget de Score circular ou radial (visual impact).
    - Adicionar cards (CTkFrame) para: OS, CPU, RAM e Disco Principal.
    - Integrar com `SystemDetector.get_profile()` para exibir dados reais.
    - Integrar com `ScoreEngine.calculate_score()`.
  </action>
  <acceptance_criteria>
    - Tela Overview carregando dados reais do hardware do usuário.
    - Score de saúde exibido de forma proeminente (0-100).
    - Design premium com espaçamento e cores harmônicas.
  </acceptance_criteria>
</task>
```
