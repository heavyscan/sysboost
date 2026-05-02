# Resumo da Execução do Plano 2.5

- Implementada detecção básica de GPU (com mockup seguro genérico sem libs pesadas externas).
- Implementada detecção de interfaces de rede (Network) filtrando loops locais através do `psutil.net_if_stats()`.
- Implementado `get_profile()`, que agrega OS, CPU, RAM, Discos, GPU e Rede, retornando a `HardwareProfile` unificada, essencial para o motor de score.
- O método `get_profile` funciona corretamente em ambiente Windows testado localmente.
