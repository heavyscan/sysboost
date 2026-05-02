---
id: "5.1"
phase: 5
wave: 1
title: "Otimização de CPU Governor (Linux)"
depends_on: []
files_modified:
  - "src/core/optimizer.py"
autonomous: true
requirements:
  - RF-05
---

# Plano 5.1 — CPU Governor (Linux)

## Objetivo

Implementar a otimização do governor de CPU no Linux, permitindo alternar para o modo "performance" em todos os núcleos para maximizar a frequência do processador.

## Tarefas

### Task 1 — Implementar CPU Governor Tuning

```xml
<task id="5.1.1">
  <title>Criar script de CPU Governor no optimizer.py</title>
  <read_first>
    - src/core/optimizer.py
  </read_first>
  <action>
    Adicionar método `optimize_linux_governor()` na classe `LinuxOptimizer` (a ser criada):
    - Verificar disponibilidade de `cpupower` ou escrever diretamente em `/sys/devices/system/cpu/cpu*/cpufreq/scaling_governor`.
    - Iterar por todos os cores e definir para `performance`.
    - Salvar o estado original para reversão.
  </action>
  <acceptance_criteria>
    - Arquivo de sistema do governor atualizado para "performance".
    - Requer privilégios de root.
  </acceptance_criteria>
</task>
```
