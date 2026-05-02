---
id: "8.1"
phase: 8
wave: 1
title: "Benchmark de CPU: Teste de Stress"
depends_on: []
files_modified:
  - "src/core/benchmark.py"
autonomous: true
requirements:
  - RF-09
---

# Plano 8.1 — Benchmark de CPU

## Objetivo

Implementar o motor de benchmark para CPU, realizando cálculos matemáticos intensivos para medir a capacidade de processamento (Single-core e Multi-core).

## Tarefas

### Task 1 — Implementar Lógica de Stress CPU

```xml
<task id="8.1.1">
  <title>Criar CPUBenchmark em benchmark.py</title>
  <action>
    Criar `src/core/benchmark.py`:
    - Implementar classe `CPUBenchmark`.
    - Criar método de stress (ex: cálculo de Pi ou números primos) que rode por X segundos.
    - Medir o tempo de execução e normalizar para um score relativo.
    - Suporte a multi-threading para medir o pico do processador.
  </action>
  <acceptance_criteria>
    - Benchmark de CPU gera uma pontuação numérica.
  </acceptance_criteria>
</task>
```
