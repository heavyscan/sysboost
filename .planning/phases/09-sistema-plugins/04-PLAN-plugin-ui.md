---
id: "9.4"
phase: 9
wave: 3
title: "UI de Gerenciamento de Plugins"
depends_on: ["9.2", "9.3"]
files_modified:
  - "src/ui/frames/plugins.py"
  - "src/ui/app.py"
autonomous: true
requirements:
  - RF-10
---

# Plano 9.4 — UI de Plugins

## Objetivo

Criar uma interface para que o usuário possa visualizar os plugins instalados, habilitar/desabilitar módulos e instalar novos plugins (via seleção de pasta).

## Tarefas

### Task 1 — Implementar PluginsFrame

```xml
<task id="9.4.1">
  <title>Criar tela de gerenciamento de plugins</title>
  <action>
    Criar `src/ui/frames/plugins.py`:
    - Listar plugins detectados pelo `PluginManager`.
    - Botão "Enable/Disable" para cada plugin.
    - Botão "Add Plugin" para copiar uma pasta externa para o diretório de plugins.
  </action>
  <acceptance_criteria>
    - Usuário gerencia plugins visualmente.
  </acceptance_criteria>
</task>
```

### Task 2 — Integrar no App

```xml
<task id="9.4.2">
  <title>Registrar PluginsFrame no app.py</title>
  <action>
    - Adicionar aba "Plugins" no menu lateral.
    - Conectar com o `PluginManager` global.
  </action>
  <acceptance_criteria>
    - Aba de plugins funcional.
  </acceptance_criteria>
</task>
```
