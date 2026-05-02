# ROADMAP.md — SysBoost

## Milestone 1: MVP Funcional

**Meta:** Ferramenta funcional com dashboard, detecção de hardware, otimizações reais e sistema de revert para os três OSes.

---

### Fase 1 — Estrutura do Projeto e Fundação

**Objetivo:** Scaffolding completo do repositório, dependências, CI/CD e arquitetura base.

**Planos:**
- `1.1` Criar estrutura de diretórios do projeto (src/, plugins/, tests/, docs/, .github/)
- `1.2` Configurar pyproject.toml, dependências (customtkinter, psutil, platformdirs) e ambiente virtual
- `1.3` Configurar GitHub Actions: lint (ruff), testes (pytest), build multiplataforma (PyInstaller)
- `1.4` Criar arquitetura base: módulos core, interfaces de plugin, sistema de logging
- `1.5` Criar README.md inicial, LICENSE (MIT) e CONTRIBUTING.md

**Saída:** Repositório pronto para desenvolvimento com CI/CD funcional

---

### Fase 2 — Engine de Detecção de Hardware e Sistema

**Objetivo:** Módulo capaz de detectar e inventariar hardware/OS de forma precisa em Windows, Linux e macOS.

**Planos:**
- `2.1` Detector de OS: versão, arquitetura, build number, modo de elevação disponível
- `2.2` Detector de CPU: modelo, fabricante (Intel/AMD/ARM), núcleos físicos/lógicos, frequência, cache
- `2.3` Detector de RAM: total, disponível, slots, tipo (DDR4/DDR5 quando acessível), frequência
- `2.4` Detector de disco: tipo (NVMe/SSD SATA/HDD), modelo, capacidade, saúde via SMART (onde possível)
- `2.5` Detector de GPU e rede: modelo GPU, VRAM, adaptadores de rede, tipo de conexão
- `2.6` Motor de score: cálculo de score 0–100 por categoria e global

**Saída:** `hardware_profile.json` gerado corretamente nos três OSes

---

### Fase 3 — Dashboard Base e Monitor em Tempo Real

**Objetivo:** Interface CustomTkinter com dark mode, navegação e gráficos ao vivo.

**Planos:**
- `3.1` Layout principal: sidebar de navegação, área de conteúdo, barra de status
- `3.2` Tela Overview: score de saúde, cards de hardware detectado, alerta de privilégios
- `3.3` Monitor em tempo real: gráficos de CPU (por core), RAM, disco I/O com histórico 60s
- `3.4` Monitor de temperatura e rede (upload/download KB/s)
- `3.5` Threading: worker em background para coleta de métricas sem travar a UI

**Saída:** Dashboard funcional com monitoramento ao vivo

---

### Fase 4 — Sistema de Otimizações Windows

**Objetivo:** Implementar todas as otimizações reais para Windows com aplicação, log e revert.

**Planos:**
- `4.1` Framework de otimizações: classe base, sistema de revert (history.json), verificação de privilégios
- `4.2` Otimizações de energia: power plans (High Performance / Ultimate Performance), desabilitar hibernação
- `4.3` Otimizações de serviços: SysMain, WSearch, DiagTrack, dmwappushservice com backup de estado
- `4.4` Otimizações de registro: visual effects, NTFS flags, Game Mode, prefetch
- `4.5` Otimizações de rede: TCP autotuning, CTCP, ECN, DNS cache flush
- `4.6` Otimizações de memória: pagefile automático baseado em RAM disponível
- `4.7` Otimizações de disco: TRIM, limpeza de temp, startup manager (listar + desabilitar)

**Saída:** Módulo Windows completo com 15+ otimizações reais e revert total

---

### Fase 5 — Sistema de Otimizações Linux

**Objetivo:** Implementar todas as otimizações reais para Linux com persistência em sysctl.conf.

**Planos:**
- `5.1` Detecção de distribuição e adaptação de comandos (systemctl vs init, cpupower vs cpufreq)
- `5.2` Otimizações de CPU: governor performance, verificação de suporte a cpufreq
- `5.3` Otimizações de memória: swappiness, vfs_cache_pressure, dirty_ratio, ZRAM
- `5.4` Otimizações de I/O: scheduler por tipo de disco (mq-deadline/bfq/none)
- `5.5` Otimizações de rede: TCP BBR, net buffers, IPv4 tuning
- `5.6` Auditor de serviços systemd: listar, classificar por impacto e desabilitar selecionados
- `5.7` Persistência: escrever alterações em /etc/sysctl.d/99-sysboost.conf + rc.local backup

**Saída:** Módulo Linux completo com persistência e revert

---

### Fase 6 — Sistema de Otimizações macOS

**Objetivo:** Implementar otimizações para macOS respeitando as restrições do SIP.

**Planos:**
- `6.1` Detecção de versão macOS, SIP status e permissões disponíveis
- `6.2` Otimizações de sistema: App Nap, animações, efeitos visuais via defaults write
- `6.3` Otimizações de Spotlight: controlar indexação por volume
- `6.4` Otimizações de rede: TCP tuning via sysctl
- `6.5` Gerenciamento de Login Items e TRIM para SSDs não-Apple
- `6.6` Backup de configurações defaults e sistema de revert via plist restore

**Saída:** Módulo macOS completo compatível com Monterey+

---

### Fase 7 — Painel Modular de Otimizações na UI

**Objetivo:** Interface para visualizar, controlar e aplicar cada otimização individualmente.

**Planos:**
- `7.1` Componente OptimizationCard: toggle, título, descrição, impacto esperado, status badge
- `7.2` Tela de otimizações por categoria (abas ou seções): CPU, RAM, Disco, Rede, Serviços, Boot
- `7.3` Wizard "Otimizar Tudo": analisa → lista recomendações → aplica com progress bar
- `7.4` Tela de histórico: log de alterações com timestamp, botão de revert por item ou sessão
- `7.5` Notificações e feedback visual durante aplicação (progress, sucesso, erro com causa)

**Saída:** UI completa e funcional para todas as otimizações

---

### Fase 8 — Engine de Benchmark Pré/Pós

**Objetivo:** Medir e exibir ganho real de desempenho antes e depois das otimizações.

**Planos:**
- `8.1` Benchmark de CPU: operações de ponto flutuante e inteiro cronometradas (score normalizado)
- `8.2` Benchmark de memória: largura de banda (MB/s) com arrays numpy
- `8.3` Benchmark de disco: leitura/escrita sequencial de arquivo temporário (MB/s)
- `8.4` Coleta de baseline automática ao abrir o app (roda em background)
- `8.5` Tela de comparativo: gráfico de barras antes/depois por categoria + ganho percentual

**Saída:** Comparativo visual com ganho mensurável para o usuário

---

### Fase 9 — Sistema de Plugins

**Objetivo:** Permitir que a comunidade adicione otimizações customizadas sem modificar o core.

**Planos:**
- `9.1` Definir interface de plugin: classe base `SysBoostPlugin` com métodos obrigatórios
- `9.2` Loader de plugins: descoberta automática em `plugins/` e `~/.sysboost/plugins/`
- `9.3` Sandbox de segurança: plugins rodam com permissões auditadas, não podem acessar dados do usuário
- `9.4` UI de plugins: tela para listar, habilitar/desabilitar e ver detalhes de plugins instalados
- `9.5` Plugin de exemplo: "Gaming Mode" que aplica conjunto de otimizações específicas para jogos

**Saída:** Sistema de plugins funcional com exemplo documentado

---

### Fase 10 — Internacionalização e Polimento

**Objetivo:** i18n, acessibilidade, tooltips e experiência de usuário refinada.

**Planos:**
- `10.1` Sistema de i18n: arquivo JSON de strings, suporte a pt-BR e en-US, detecção automática do locale
- `10.2` Tooltips detalhados em todas as otimizações (o que faz, impacto, reversibilidade)
- `10.3` Onboarding: tela de boas-vindas, detecção automática na primeira execução, resumo do que foi encontrado
- `10.4` Tratamento de erros: mensagens amigáveis, fallbacks para cada otimização que falhar
- `10.5` Polimento visual: animações suaves, estados de loading, dark/light mode toggle

**Saída:** Produto polido e pronto para usuários finais

---

### Fase 11 — Build, Empacotamento e Distribuição

**Objetivo:** Criar executáveis distribuíveis para os três OSes via CI/CD automatizado.

**Planos:**
- `11.1` Configuração PyInstaller: spec files para Windows (.exe com ícone, sem console)
- `11.2` Configuração PyInstaller: AppImage para Linux (usando linuxdeploy)
- `11.3` Configuração PyInstaller: .app para macOS com assinatura ad-hoc
- `11.4` GitHub Actions: workflow de release automático ao criar tag vX.Y.Z
- `11.5` GitHub Releases: upload automático dos artefatos com changelog gerado

**Saída:** `SysBoost-v1.0.0.exe`, `SysBoost-v1.0.0.AppImage`, `SysBoost-v1.0.0.app`

---

### Fase 12 — Testes, Documentação Final e Lançamento

**Objetivo:** Cobertura de testes, documentação completa e preparação para lançamento público.

**Planos:**
- `12.1` Testes unitários para todos os módulos de detecção e otimização (mock de sistema)
- `12.2` Testes de integração: execução em VM Windows, Linux e macOS
- `12.3` README completo: badges, screenshots do dashboard, GIF de demo, instalação, uso, contribuição
- `12.4` Wiki do GitHub: documentação de plugins, referência de otimizações, FAQ
- `12.5` Checklist de lançamento: segurança, legal (MIT), código limpo, issues template, discussions habilitado

**Saída:** Projeto pronto para lançamento público no GitHub

---

## Status

| Fase | Nome | Status | Planos |
|------|------|--------|--------|
| 1 | Estrutura e Fundação | ● Concluída | 5 planos |
| 2 | Detecção de Hardware | ● Concluída | 6 planos |
| 3 | Dashboard e Monitor | ● Concluída | 5 planos |
| 4 | Otimizações Windows | ● Concluída | 7 planos |
| 5 | Otimizações Linux | ● Concluída | 7 planos |
| 6 | Otimizações macOS | ● Concluída | 6 planos |
| 7 | Painel Modular UI | ● Concluída | 5 planos |
| 8 | Engine de Benchmark | ● Concluída | 5 planos |
| 9 | Sistema de Plugins | ● Concluída | 5 planos |
| 10 | i18n e Polimento | ● Concluída | 5 planos |
| 11 | Build e Distribuição | ● Concluída | 5 planos |
| 12 | Testes e Lançamento | ● Concluída | 5 planos |

**Total:** 12 fases · 66 planos (100% Concluído)
