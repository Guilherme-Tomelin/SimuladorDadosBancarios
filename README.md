   Simulador de Dados Bancários
   Documentação dos requisitos e funcionalidades.

1. Introdução:
   - O Simulador de Dados Bancários é uma ferramenta desenvolvida para auxiliar no desenvolvimento do projeto financial_transactions.
   - O objetivo do simulador é gerar dados bancários simulados que podem ser utilizados para testes, validações e desenvolvimento do projeto principal.
   - Link do projeto mencionado: https://github.com/Guilherme-Tomelin/financial_transactions

2. Requisitos Funcionais / Usabilidade:
   - Geração de dados simulados: O simulador deve ser capaz de gerar dados simulados para bancos, contas, valores de transações e datas.
   - Definição do número de linhas: O usuário deve ter a opção de definir o número de linhas de dados a serem gerados no arquivo CSV simulado.
   - Seleção de características dos dados: O usuário deve poder escolher quais características dos dados bancários deseja incluir na simulação, como nome do banco, número da conta, valores, datas, entre outros.
   - Desempenho: O simulador deve ser eficiente e capaz de gerar grandes volumes de dados simulados de forma rápida.
   - Usabilidade: Interface intuitiva e fácil de usar.

3. Formato dos Arquivos CSV:
   - O formato dos arquivos CSV gerados pelo simulador deve seguir a estrutura abaixo:
      - Nome do banco (texto)
      - Número da conta (texto)
      - Nome do banco destinatário (texto)
      - Número da conta destinatária (texto)
      - Valor da transação (numérico)
      - Data e hora da transação (formato ISO 8601)

   Exemplo do formato esperado dos dados no arquivo CSV:
   ```csv
   BANCO BANRISUL,0001,00001-1,BANCO BRADESCO,0001,00001-1,250,2022-05-01T16:30:00
   BANCO ITAU,0001,00001-1,BANCO BRADESCO,0001,00001-1,8900.75,2022-05-01T16:55:00
   ```

4. Restrições e Limitações:
   - O Simulador de Dados Bancários está sendo desenvolvido exclusivamente para auxiliar o projeto financial_transactions, portanto, seu uso é restrito a esse contexto.
   - O simulador não realiza transações reais, apenas gera dados simulados com finalidade de teste e desenvolvimento.
   - Não são permitidas a inclusão de informações reais ou sensíveis nos dados simulados.
