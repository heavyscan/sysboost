# SysBoost — Otimizador de Desempenho Multiplataforma

## O Que É Este Projeto

**SysBoost** é uma ferramenta open source de otimização de desempenho com dashboard visual (Python + CustomTkinter) que detecta automaticamente o hardware e o sistema operacional da máquina, aplica tuning real e profundo em CPU, RAM, disco, rede, serviços e boot — tudo em um painel moderno com monitoramento em tempo real.

**Diferenciais:**
- Não é um "limpador" superficial — aplica otimizações a nível de kernel, registro, drivers e scheduler
- Adaptativo: cada máquina recebe um perfil de otimização personalizado baseado no seu hardware detectado
- Transparente: mostra exatamente o que foi alterado, com antes/depois e opção de reverter
- Multiplataforma real: Windows, Linux e macOS com lógica nativa para cada OS

## Contexto

- **Tipo:** Greenfield — projeto novo do zero
- **Público:** Comunidade open source (GitHub), usuários técnicos e entusiastas de performance
- **Linguagem:** Python 3.11+
- **UI:** CustomTkinter (dark mode, moderna, distribuível como executável)
- **Distribuição:** PyInstaller → `.exe` (Windows), binário AppImage (Linux), `.app` (macOS)
- **Repositório:** GitHub (open source, licença MIT)
- **OS Alvo:** Windows 10/11, Ubuntu/Debian/Arch Linux, macOS 12+

## Problema Central

Ferramentas de otimização existentes são:
- Superficiais (só limpam temp e startup)
- Específicas de plataforma (só Windows)
- Pagas ou com freemium irritante
- Sem transparência sobre o que realmente fazem

SysBoost resolve isso entregando otimizações reais, cross-platform, gratuitas e com total visibilidade.

## Requisitos

### Validados

(Nenhum ainda — greenfield)

### Ativos

**Core — Detecção e Análise:**
- [ ] Detectar OS, versão, arquitetura automaticamente
- [ ] Coletar inventário de hardware: CPU (modelo, cores, threads, freq), RAM (total, tipo, frequência), disco (tipo SSD/HDD, capacidade), GPU, rede
- [ ] Gerar perfil de otimização personalizado por máquina
- [ ] Benchmark rápido pré e pós-otimização para medir ganho real

**Core — Otimizações Reais (Windows):**
- [ ] Trocar power plan para High Performance / Ultimate Performance
- [ ] Desabilitar SysMain (SuperFetch) e Windows Search se não necessário
- [ ] Tuning de registro: visual effects, prefetch, NTFS, GameMode
- [ ] Desabilitar telemetria e serviços desnecessários (lista curada)
- [ ] TCP stack tuning (autotuning, congestion provider, ECN)
- [ ] Disable HPET se benéfico para o hardware
- [ ] Gerenciar programas de startup
- [ ] Disk cleanup automatizado + TRIM para SSDs
- [ ] Otimizar virtual memory (pagefile) baseado na RAM disponível

**Core — Otimizações Reais (Linux):**
- [ ] CPU governor → performance (via cpupower/cpufreq)
- [ ] Ajustar swappiness e cache_pressure baseado na RAM
- [ ] Configurar I/O scheduler (mq-deadline para SSD, bfq para HDD)
- [ ] TCP BBR como congestion control
- [ ] Otimizar vm.dirty_ratio e vm.dirty_writeback_centisecs
- [ ] Auditar e desabilitar serviços systemd desnecessários
- [ ] Configurar ZRAM se RAM < 8GB
- [ ] IRQ affinity para máquinas multicore
- [ ] Hugepages para workloads específicos

**Core — Otimizações Reais (macOS):**
- [ ] Desabilitar App Nap para apps pesados
- [ ] Controlar indexação do Spotlight
- [ ] Gerenciar Login Items
- [ ] TCP tuning via sysctl
- [ ] Desabilitar efeitos visuais desnecessários
- [ ] Purge de memória inativa
- [ ] TRIM management para SSDs não-Apple

**Dashboard Visual:**
- [ ] Tela inicial com visão geral do sistema (hardware detectado + score de saúde)
- [ ] Monitor em tempo real: CPU %, RAM %, disco I/O, temperatura, rede (gráficos animados)
- [ ] Painel modular: cada categoria de otimização com toggle on/off e descrição do impacto
- [ ] Wizard de otimização: analisa → recomenda → aplica com confirmação
- [ ] Log de alterações: o que foi feito, quando, com opção de reverter
- [ ] Comparativo antes/depois: métricas de benchmark pré e pós

**Distribuição e Open Source:**
- [ ] PyInstaller build para os três OSes (CI/CD via GitHub Actions)
- [ ] README profissional com screenshots, instalação e uso
- [ ] Licença MIT
- [ ] CONTRIBUTING.md para a comunidade
- [ ] Sistema de plugins para a comunidade adicionar otimizações

### Fora de Escopo

- Overclocking de hardware — risco de dano físico, fora do escopo v1
- Otimizações de jogos específicos — foco em desempenho geral do sistema
- Antivírus / limpeza de malware — escopo diferente
- Suporte a Windows 7/8 — sistemas muito antigos, APIs limitadas

## Decisões Técnicas

| Decisão | Racional | Resultado |
|---------|----------|-----------|
| Python + CustomTkinter | Cross-platform nativo, acesso profundo ao sistema, UI moderna, distribuição via PyInstaller | Adotado |
| Licença MIT | Máxima adoção pela comunidade, sem fricção | Adotado |
| Arquitetura modular (plugins) | Permite comunidade contribuir otimizações sem tocar no core | Adotado |
| PyInstaller para distribuição | Um executável, sem dependências para o usuário final | Adotado |
| Revert system | Transparência e segurança — usuário pode desfazer qualquer mudança | Adotado |

## Evolução

Este documento evolui a cada transição de fase e milestone.

**Após cada fase:** atualizar Requisitos (Validados/Ativos/Fora de Escopo) e Decisões Técnicas.
**Após cada milestone:** revisão completa + verificação de aderência ao Core Value.

---
*Última atualização: 2026-05-01 — Inicialização do projeto*
