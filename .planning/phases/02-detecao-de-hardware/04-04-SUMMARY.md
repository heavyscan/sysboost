# Resumo da Execução do Plano 2.4

- Implementada detecção de discos e partições com a biblioteca `psutil`.
- Ignoradas partições virtuais e unmonted para evitar exceções indesejadas.
- Tratamento de exceções `PermissionError` para acessos negados a certas partições.
- Testado no ambiente local exibindo informações corretas sobre `C:\`, `D:\`, `E:\`, e `F:\`.
