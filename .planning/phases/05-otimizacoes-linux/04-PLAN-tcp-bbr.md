---
id: "5.4"
phase: 5
wave: 2
title: "Ativação de TCP BBR e Tuning de Rede"
depends_on: []
files_modified:
  - "src/core/optimizer.py"
autonomous: true
requirements:
  - RF-05
---

# Plano 5.4 — TCP BBR e Rede (Linux)

## Objetivo

Ativar o algoritmo de controle de congestionamento TCP BBR do Google e otimizar buffers de rede para melhor performance em conexões de alta latência ou instáveis.

## Tarefas

### Task 1 — Ativar BBR e Tunar Buffers

```xml
<task id="5.4.1">
  <title>Configurar rede avançada via sysctl</title>
  <read_first>
    - src/core/optimizer.py
  </read_first>
  <action>
    Adicionar método `optimize_linux_network()`:
    - Ativar BBR: `net.ipv4.tcp_congestion_control=bbr`.
    - Definir qdisc: `net.core.default_qdisc=fq`.
    - Tunar buffers: `net.core.rmem_max`, `net.core.wmem_max`, etc.
  </action>
  <acceptance_criteria>
    - Comandos sysctl aplicados com sucesso.
  </acceptance_criteria>
</task>
```
