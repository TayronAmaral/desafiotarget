Desafio Target
Este repositório contém a solução para um conjunto de desafios de programação. O código foi desenvolvido em Python, abordando os seguintes problemas:

Questões
1. Cálculo da soma dos números de 1 até um valor específico
Dado o trecho de código:

python
Copiar
Editar
int INDICE = 13, SOMA = 0, K = 0;
Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
Imprimir(SOMA);
Ao final do processamento, a variável SOMA conterá o valor da soma dos números de 1 a 13. O programa calcula a soma de todos os números inteiros de 1 até 13.

2. Verificação de número na sequência de Fibonacci
O programa calcula a sequência de Fibonacci até um número informado e verifica se o número informado pertence ou não à sequência. A sequência de Fibonacci é formada por números onde cada termo é a soma dos dois anteriores, começando por 0 e 1.

3. Análise do faturamento mensal
Um vetor contém os valores de faturamento diário de uma distribuidora. O programa calcula e retorna:

O menor valor de faturamento ocorrido em um dia do mês.
O maior valor de faturamento ocorrido em um dia do mês.
O número de dias no mês em que o faturamento diário foi superior à média mensal.
Nota: Para o cálculo da média, dias sem faturamento (como finais de semana e feriados) devem ser ignorados.

4. Cálculo do percentual de representação por estado
Dado o faturamento mensal por estado de uma distribuidora:

SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53
O programa calcula o percentual de representação de cada estado no faturamento total mensal.

5. Inversão de uma string
O programa inverte os caracteres de uma string fornecida, sem utilizar funções prontas como reverse.

Tecnologias Utilizadas
Python (ou outra linguagem de sua escolha)
JSON/XML para manipulação de dados

Como Rodar o Código:
Passo 1: Clone o Repositório
Para clonar o repositório, execute o seguinte comando no seu terminal:

bash
Copiar
Editar
git clone https://github.com/TayronAmaral/desafiotarget.git
Passo 2: Navegue para o Diretório
Entre no diretório do projeto:

bash
Copiar
Editar
cd desafiotarget
Passo 3: Execute os Programas
Execute o código referente a cada questão. Por exemplo, para a questão 1, execute:

bash
Copiar
Editar
python questao1.py
Repita o processo para as outras questões, executando os arquivos correspondentes.
