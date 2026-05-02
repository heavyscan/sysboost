---
id: "11.4"
phase: 11
wave: 3
title: "Validação do Binário Portable"
depends_on: ["11.3"]
files_modified: []
autonomous: true
requirements:
  - RF-11
---

# Plano 11.4 — Teste de Executável

## Objetivo

Verificar se o executável gerado funciona de forma independente (portable) em uma máquina limpa, sem a necessidade de ter o Python instalado.

## Tarefas

### Task 1 — Verificação de Dependências Embutidas

```xml
<task id="11.4.1">
  <title>Executar teste de fumaça no binário</title>
  <action>
    - Rodar o executável da pasta `dist/`.
    - Verificar se todas as telas carregam.
    - Confirmar que as traduções JSON e o `psutil` estão funcionando no binário.
  </action>
  <acceptance_criteria>
    - Executável abre sem erros e monitora sistema.
  </acceptance_criteria>
</task>
```
