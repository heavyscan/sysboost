# Resumo da Execução do Plano 2.2

- Implementada detecção de CPU utilizando a biblioteca `psutil`.
- Método `SystemDetector.get_cpu_info()` coleta modelo, contagem de núcleos (físicos e lógicos) e frequências base/max.
- Implementada uma lógica básica para obter o fabricante a partir do nome do processador.
- Testado e funcionou com sucesso.
