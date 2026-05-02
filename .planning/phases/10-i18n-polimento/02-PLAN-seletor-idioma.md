---
id: "10.2"
phase: 10
wave: 1
title: "Troca Dinâmica de Idioma"
depends_on: ["10.1"]
files_modified:
  - "src/ui/frames/settings.py"
  - "src/i18n/__init__.py"
autonomous: true
requirements:
  - RF-10
---

# Plano 10.2 — Seletor de Idioma

## Objetivo

Implementar a funcionalidade de trocar o idioma do aplicativo em tempo real através da aba de configurações.

## Tarefas

### Task 1 — Implementar SettingsFrame

```xml
<task id="10.2.1">
  <title>Criar tela de configurações com seletor de idioma</title>
  <action>
    Criar `src/ui/frames/settings.py`:
    - Adicionar um `ctk.CTkOptionMenu` com as opções "Português" e "English".
    - Ao trocar, atualizar a configuração global e forçar o refresh das labels (ou exibir aviso de reinicialização).
  </action>
  <acceptance_criteria>
    - Usuário consegue trocar o idioma na UI.
  </acceptance_criteria>
</task>
```
