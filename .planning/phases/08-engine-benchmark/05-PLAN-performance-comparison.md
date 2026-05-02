---
id: "8.5"
phase: 8
wave: 3
title: "Comparativo Antes vs Depois"
depends_on: ["8.3", "8.4"]
files_modified:
  - "src/ui/frames/benchmark.py"
autonomous: true
requirements:
  - RF-09
---

# Plano 8.5 — Comparativo de Performance

## Objetivo

Implementar uma visualização comparativa que mostra o ganho (ou perda) de performance após a aplicação das otimizações do SysBoost.

## Tarefas

### Task 1 — Implementar Visualização de Ganhos

```xml
<task id="8.5.1">
  <title>Criar gráfico ou tabela comparativa</title>
  <action>
    Atualizar `BenchmarkFrame`:
    - Comparar o benchmark atual com o primeiro benchmark realizado (baseline).
    - Mostrar porcentagem de ganho: "+15% Performance".
    - Usar cores (Verde para ganho, Vermelho para perda).
  </action>
  <acceptance_criteria>
    - Usuário visualiza claramente o benefício das otimizações.
  </acceptance_criteria>
</task>
```
