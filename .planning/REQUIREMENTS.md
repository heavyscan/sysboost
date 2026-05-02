# REQUIREMENTS.md — SysBoost

## Milestone 1: Fundação e MVP

### Requisitos Funcionais

#### RF-01 — Detecção de Sistema
- O sistema deve detectar o OS (Windows/Linux/macOS), versão e arquitetura ao iniciar
- O sistema deve inventariar CPU (modelo, núcleos, threads, frequência base/turbo)
- O sistema deve inventariar RAM (total, disponível, tipo se detectável)
- O sistema deve identificar tipo de disco (SSD NVMe / SSD SATA / HDD) por unidade
- O sistema deve detectar GPU (modelo, VRAM, fabricante)
- O sistema deve detectar adaptadores de rede

#### RF-02 — Score de Saúde
- O sistema deve calcular um score de 0–100 para o estado atual de otimização
- O score deve ser composto por sub-scores por categoria (CPU, RAM, Disco, Rede, Serviços)
- O score deve refletir otimizações já aplicadas vs. potencial disponível

#### RF-03 — Dashboard em Tempo Real
- O dashboard deve exibir uso de CPU (%) por núcleo e total, atualizado a cada 1s
- O dashboard deve exibir uso de RAM (%), memória livre e em cache
- O dashboard deve exibir I/O de disco (leitura/escrita MB/s) por unidade
- O dashboard deve exibir temperatura de CPU (quando disponível via sensores)
- O dashboard deve exibir throughput de rede (upload/download KB/s)
- Os gráficos devem ter histórico dos últimos 60 segundos

#### RF-04 — Otimizações Windows
- Alterar power plan para High Performance ou Ultimate Performance
- Desabilitar SysMain (SuperFetch) via sc.exe + registry
- Desabilitar Windows Search indexing (serviço WSearch)
- Aplicar visual effects → "Adjust for best performance" via SystemParametersInfo
- Tuning de registro NTFS (NtfsDisable8dot3NameCreation, NtfsMemoryUsage)
- Ativar Game Mode (GameConfigStore)
- TCP stack: autotuning normal, congestion provider=ctcp, ECN desabilitado
- Desabilitar telemetria (DiagTrack, dmwappushservice)
- Configurar pagefile automaticamente (1.5x RAM se < 16GB, fixo 4096MB se > 16GB)
- Gerenciar programas de startup (listar + desabilitar selecionados)
- Disk TRIM manual para SSDs (defrag /retrim)
- Desabilitar hibernação (powercfg /h off) em desktops

#### RF-05 — Otimizações Linux
- Alterar CPU governor para "performance" via cpufreq-set ou echo direto em /sys
- Ajustar vm.swappiness (10 se RAM ≥ 8GB, 30 se RAM < 8GB)
- Ajustar vm.vfs_cache_pressure (50)
- Ajustar vm.dirty_ratio e vm.dirty_writeback_centisecs
- Configurar I/O scheduler: mq-deadline para SSD, bfq para HDD via /sys/block/*/queue/scheduler
- Ativar TCP BBR: net.ipv4.tcp_congestion_control=bbr + net.core.default_qdisc=fq
- Otimizar net buffers: net.core.rmem_max, wmem_max, net.ipv4.tcp_rmem, tcp_wmem
- Auditar serviços systemd: listar habilitados e recomendar desabilitação de não essenciais
- Configurar ZRAM se RAM ≤ 8GB
- Persistir alterações em /etc/sysctl.conf e /etc/rc.local

#### RF-06 — Otimizações macOS
- Desabilitar App Nap: defaults write NSGlobalDomain NSAppSleepDisabled -bool YES
- Controlar Spotlight: launchctl unload -w /System/Library/LaunchDaemons/com.apple.metadata.mds.plist
- TCP tuning via sysctl: net.inet.tcp.delayed_ack=0, kern.ipc.somaxconn
- Desabilitar efeitos visuais: NSAutomaticWindowAnimationsEnabled, com.apple.universalaccess
- Verificar e ativar TRIM para SSDs via trimforce
- Listar e gerenciar Login Items via osascript

#### RF-07 — Sistema de Revert
- Cada otimização aplicada deve ser registrada em `.sysboost/history.json` com valor anterior
- O usuário deve poder reverter qualquer otimização individual ou todas de uma sessão
- O revert deve restaurar exatamente o valor original detectado antes da mudança

#### RF-08 — Painel Modular
- Cada categoria de otimização deve ter uma seção separada no dashboard
- Cada otimização individual deve ter: toggle on/off, descrição do impacto esperado, status (aplicada/pendente/incompatível)
- O usuário deve poder aplicar otimizações individualmente ou por categoria completa

#### RF-09 — Benchmark Pré/Pós
- Executar benchmark sintético de CPU (operações matemáticas cronometradas)
- Executar benchmark de memória (largura de banda)
- Executar benchmark de disco (leitura sequencial MB/s via teste de arquivo temporário)
- Exibir comparativo antes/depois ao final da sessão de otimização

#### RF-10 — Distribuição
- Build automatizado via GitHub Actions para Windows (.exe via PyInstaller), Linux (AppImage), macOS (.app)
- README com screenshots, instruções de instalação e uso
- CONTRIBUTING.md com guia para a comunidade
- Licença MIT
- Sistema de plugins: diretório `plugins/` com interface definida para adicionar otimizações customizadas

### Requisitos Não-Funcionais

#### RNF-01 — Segurança
- Operações privilegiadas devem solicitar elevação explicitamente (UAC no Windows, sudo no Linux/macOS)
- Nenhuma otimização deve ser aplicada sem consentimento explícito do usuário
- O sistema deve validar que está rodando com privilégios suficientes antes de cada operação

#### RNF-02 — Performance
- O dashboard deve iniciar em menos de 3 segundos
- A detecção de hardware deve completar em menos de 5 segundos
- O monitoramento em tempo real não deve consumir mais de 2% de CPU

#### RNF-03 — Compatibilidade
- Windows: 10 (1903+) e 11
- Linux: Ubuntu 20.04+, Debian 11+, Arch Linux (rolling), Fedora 36+
- macOS: Monterey (12) e superiores
- Python: 3.11+

#### RNF-04 — Usabilidade
- Interface em português e inglês (i18n básico)
- Dark mode por padrão
- Tooltips explicativos em cada otimização
- Log de atividade visível em tempo real durante aplicação

### Critérios de Aceitação (UAT)

| ID | Cenário | Critério de Sucesso |
|----|---------|---------------------|
| UAT-01 | Usuário abre o app no Windows | Hardware detectado corretamente em < 5s, score exibido |
| UAT-02 | Usuário aplica todas as otimizações Windows | Power plan alterado, serviços desabilitados, registry atualizado, log registra tudo |
| UAT-03 | Usuário reverte todas as otimizações | Sistema retorna ao estado pré-otimização verificado |
| UAT-04 | Usuário roda benchmark pré/pós | Melhoria mensurável exibida (esperado: +5% a +30% dependendo da máquina) |
| UAT-05 | App roda no Linux sem modificações | Detecção + otimizações aplicadas corretamente |
| UAT-06 | App roda no macOS sem modificações | Detecção + otimizações aplicadas corretamente |
| UAT-07 | Usuário baixa o .exe e roda sem Python | Executa sem instalar dependências |
| UAT-08 | Monitor em tempo real | Gráficos atualizam a cada 1s sem travar a UI |
