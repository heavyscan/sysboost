# Resumo da Execução do Plano 2.3

- Implementada detecção de Memória RAM com a biblioteca `psutil`.
- Método `SystemDetector.get_ram_info()` retorna capacidade total e disponível em gigabytes (GB), formatado com precisão.
- Adicionada leitura de `used_percent` para obter a porcentagem utilizada diretamente do SO.
- Testado e funcionou com sucesso.
