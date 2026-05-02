---
id: "1.5"
phase: 1
wave: 3
title: "Criar README.md, LICENSE e CONTRIBUTING.md"
depends_on: ["1.1", "1.2", "1.3"]
files_modified:
  - "README.md"
  - "LICENSE"
  - "CONTRIBUTING.md"
  - "CHANGELOG.md"
  - "SECURITY.md"
autonomous: true
requirements:
  - RF-10
---

# Plano 1.5 — README.md, LICENSE (MIT) e CONTRIBUTING.md

## Objetivo

Criar toda a documentação de repositório necessária para um projeto open source profissional no GitHub: README com badges e instruções claras, LICENSE MIT, CONTRIBUTING.md para novos contribuidores, CHANGELOG e SECURITY policy.

## Tarefas

### Task 1 — README.md completo

```xml
<task id="1.5.1">
  <title>Criar README.md profissional para o GitHub</title>
  <read_first>
    - F:\Automações\customização\.planning\PROJECT.md
    - F:\Automações\customização\.planning\REQUIREMENTS.md
  </read_first>
  <action>
    Criar `README.md` na raiz do projeto com o seguinte conteúdo:

    ```markdown
    <div align="center">

    # ⚡ SysBoost

    **Otimizador de desempenho multiplataforma com dashboard visual**

    [![CI](https://github.com/sysboost/sysboost/actions/workflows/ci.yml/badge.svg)](https://github.com/sysboost/sysboost/actions)
    [![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://python.org)
    [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
    [![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)](README.md)

    [🇧🇷 Português](docs/README.pt-BR.md) · [Download](#-instalação) · [Contribuir](CONTRIBUTING.md)

    </div>

    ---

    ## 🚀 O que é o SysBoost?

    SysBoost é uma ferramenta open source que detecta automaticamente o hardware da sua máquina e aplica **otimizações reais de desempenho** — não apenas limpeza superficial de arquivos temporários.

    **O que ele realmente faz:**
    - 🔧 Ajusta power plans, CPU governor e parâmetros do kernel
    - 💾 Otimiza memória virtual, swappiness e gestão de cache
    - 🌐 Faz tuning do stack TCP/IP para menor latência
    - 🗑️ Desabilita serviços desnecessários com backup para reverter
    - 📊 Monitora CPU, RAM, disco e temperatura em tempo real

    ## 📦 Instalação

    ### Download direto (sem Python)
    Baixe o executável para seu sistema na [página de Releases](https://github.com/sysboost/sysboost/releases).

    | Sistema | Download |
    |---------|----------|
    | Windows 10/11 | `SysBoost.exe` |
    | Linux (Ubuntu/Arch/Fedora) | `SysBoost.AppImage` |
    | macOS 12+ | `SysBoost.app` |

    > ⚠️ **Windows:** Executar como Administrador para otimizações completas.
    > **Linux/macOS:** `sudo ./SysBoost` para otimizações de kernel.

    ### Do código-fonte

    ```bash
    git clone https://github.com/sysboost/sysboost.git
    cd sysboost
    python scripts/setup_dev.py
    source .venv/bin/activate  # Linux/macOS
    # .venv\Scripts\activate   # Windows
    python main.py
    ```

    ## 🖥️ Screenshots

    > *Screenshots serão adicionados após a implementação da UI (Fase 3)*

    ## 🔬 Otimizações Disponíveis

    | Categoria | Windows | Linux | macOS |
    |-----------|:-------:|:-----:|:-----:|
    | Power Plan / CPU Governor | ✅ | ✅ | ✅ |
    | RAM / Swappiness | ✅ | ✅ | ✅ |
    | Disco / I/O Scheduler | ✅ | ✅ | ✅ |
    | Rede / TCP Tuning | ✅ | ✅ | ✅ |
    | Serviços Desnecessários | ✅ | ✅ | ✅ |
    | Boot / Startup | ✅ | ✅ | ✅ |

    ## 🔌 Plugins

    SysBoost suporta plugins da comunidade. Crie seu próprio:

    ```python
    from src.plugins.base import SysBoostPlugin, OptimizationResult

    class MeuPlugin(SysBoostPlugin):
        name = "meu-plugin"
        display_name = "Meu Plugin"
        description = "Descrição do que faz"
        supported_os = ["windows", "linux", "darwin"]

        def is_applicable(self) -> bool:
            return True

        def apply(self) -> OptimizationResult:
            # Aplicar otimização
            return OptimizationResult(success=True, message="Aplicado!")

        def revert(self, revert_data: dict) -> OptimizationResult:
            # Reverter otimização
            return OptimizationResult(success=True, message="Revertido!")
    ```

    Coloque em `plugins/meu-plugin/__init__.py` e o SysBoost carregará automaticamente.

    ## 🤝 Contribuindo

    Leia [CONTRIBUTING.md](CONTRIBUTING.md) para começar.

    ## 📄 Licença

    MIT License — veja [LICENSE](LICENSE) para detalhes.
    ```
  </action>
  <acceptance_criteria>
    - `README.md` existe
    - Arquivo contém `# ⚡ SysBoost`
    - Arquivo contém `[![CI]`
    - Arquivo contém `## 🔬 Otimizações Disponíveis`
    - Arquivo contém `## 🔌 Plugins`
    - Arquivo contém `class MeuPlugin(SysBoostPlugin):`
    - Arquivo tem mais de 80 linhas
  </acceptance_criteria>
</task>
```

### Task 2 — LICENSE, CONTRIBUTING.md e CHANGELOG

```xml
<task id="1.5.2">
  <title>Criar LICENSE MIT, CONTRIBUTING.md, CHANGELOG e SECURITY</title>
  <read_first>
    - README.md (após Task 1.5.1)
  </read_first>
  <action>
    Criar `LICENSE` com texto MIT completo:
    ```
    MIT License

    Copyright (c) 2026 SysBoost Contributors

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
    ```

    Criar `CONTRIBUTING.md` com guia para contribuidores:
    ```markdown
    # Contribuindo com o SysBoost

    Obrigado por querer contribuir! 🎉

    ## Como Começar

    1. Fork o repositório
    2. Clone seu fork: `git clone https://github.com/SEU-USER/sysboost.git`
    3. Configure o ambiente: `python scripts/setup_dev.py`
    4. Crie uma branch: `git checkout -b feature/minha-feature`
    5. Faça as mudanças e adicione testes
    6. Verifique: `make lint && make test`
    7. Commit: `git commit -m "feat: descrição clara da mudança"`
    8. Push e abra um Pull Request

    ## Tipos de Contribuição

    - 🐛 **Bug fixes** — sempre bem-vindos!
    - ✨ **Novas otimizações** — veja a estrutura de plugins
    - 🌍 **Traduções** — adicione arquivos em `src/i18n/`
    - 📚 **Documentação** — melhore o README ou a Wiki
    - 🧪 **Testes** — aumente a cobertura de testes

    ## Adicionando uma Nova Otimização

    1. Crie um plugin em `plugins/nome-da-otimizacao/`
    2. Estenda `SysBoostPlugin` de `src/plugins/base.py`
    3. Implemente `apply()` com sistema de revert
    4. Adicione testes em `tests/unit/test_nome.py`
    5. Documente no PR o que a otimização faz e por quê

    ## Convenções de Commit

    Usamos [Conventional Commits](https://conventionalcommits.org):
    - `feat:` nova funcionalidade
    - `fix:` correção de bug
    - `docs:` documentação
    - `test:` testes
    - `refactor:` refatoração sem mudança de comportamento
    - `chore:` manutenção (deps, CI, etc.)

    ## Code Style

    Usamos `ruff` para lint e formatação:
    ```bash
    make lint    # verificar
    make format  # corrigir automaticamente
    ```

    ## Reportando Bugs

    Use o template de [Bug Report](.github/ISSUE_TEMPLATE/bug_report.md).
    Inclua sempre: OS, versão do SysBoost, passos para reproduzir.
    ```

    Criar `CHANGELOG.md`:
    ```markdown
    # Changelog

    Todas as mudanças notáveis serão documentadas aqui.

    Formato baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/).

    ## [Unreleased]

    ### Added
    - Estrutura inicial do projeto
    - Interface base de plugins (SysBoostPlugin)
    - Sistema de i18n (pt-BR e en-US)
    - CI/CD com GitHub Actions
    ```

    Criar `SECURITY.md`:
    ```markdown
    # Política de Segurança

    ## Reportando Vulnerabilidades

    **Não abra issues públicas para vulnerabilidades de segurança.**

    Envie um email para: security@sysboost.app (substitua pelo email real)

    Incluir:
    - Descrição da vulnerabilidade
    - Passos para reproduzir
    - Impacto potencial

    Responderemos em até 48 horas.

    ## Notas de Segurança

    O SysBoost requer privilégios elevados para algumas operações.
    Todas as otimizações são documentadas e reversíveis.
    Nunca coleta ou transmite dados do usuário.
    ```
  </action>
  <acceptance_criteria>
    - `LICENSE` existe e contém `MIT License`
    - `LICENSE` contém `Copyright (c) 2026 SysBoost Contributors`
    - `CONTRIBUTING.md` existe e contém `## Como Começar`
    - `CONTRIBUTING.md` contém `SysBoostPlugin`
    - `CHANGELOG.md` existe e contém `## [Unreleased]`
    - `SECURITY.md` existe e contém `Reportando Vulnerabilidades`
  </acceptance_criteria>
</task>
```

## Must-Haves

- [ ] `README.md` profissional com badges, tabela de otimizações e exemplo de plugin
- [ ] `LICENSE` com texto MIT completo
- [ ] `CONTRIBUTING.md` com guia claro para novos contribuidores
- [ ] `CHANGELOG.md` iniciado
- [ ] `SECURITY.md` com política de reporte
