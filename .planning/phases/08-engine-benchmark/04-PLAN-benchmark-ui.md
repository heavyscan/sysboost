---
id: "8.4"
phase: 8
wave: 2
title: "Interface de Benchmark: Execução e Visualização"
depends_on: ["8.1", "8.2"]
files_modified:
  - "src/ui/frames/benchmark.py"
  - "src/ui/app.py"
autonomous: true
requirements:
  - RF-09
---

# Plano 8.4 — Interface de Benchmark

## Objetivo

Criar a tela de benchmark onde o usuário pode iniciar os testes e visualizar os resultados em tempo real.

## Tarefas

### Task 1 — Implementar BenchmarkFrame

```xml
<task id="8.4.1">
  <title>Criar tela de Benchmark na UI</title>
  <action>
    Criar `src/ui/frames/benchmark.py`:
    - Botões para iniciar "Quick Test" ou "Deep Test".
    - Indicadores de progresso durante o stress da CPU.
    - Exibição dos scores finais de CPU e Velocidades de Disco.
  </action>
  <acceptance_criteria>
    - Usuário consegue iniciar e ver o resultado do teste pela UI.
  </acceptance_criteria>
</task>
```

### Task 2 — Integrar no App

```xml
<task id="8.4.2">
  <title>Registrar BenchmarkFrame no app.py</title>
  <action>
    Atualizar `src/ui/app.py`:
    - Importar e inicializar `BenchmarkFrame`.
    - Substituir o placeholder pela instância real.
  </action>
  <acceptance_criteria>
    - Navegação para a aba "Benchmark" funciona.
  </acceptance_criteria>
</task>
```
