
## Validador de Entrada
Este é um aplicativo construído em Python com interface gráfica usando Tkinter. 
Ele permite validar diferentes tipos de entradas de acordo com expressões regulares predefinidas.

## Funcionalidades
- Seleção de Tipo de Validação: Escolha o tipo de validação a ser aplicado a partir de uma lista pré-definida, como Dígito, Decimal, Letra, URL, E-mail, entre outros.

- Atualização Automática da Expressão Regular: Quando um tipo de validação é selecionado, a expressão regular correspondente é automaticamente exibida.

- Validação de Entrada: Insira um valor e clique no botão "Validar" para verificar se ele corresponde ao tipo selecionado.

## Tipos de Validação Suportados

- ```Dígito```: Verifica se a entrada contém apenas dígitos.

- ```Decimal```: Verifica se a entrada é um número decimal válido.

- ```Letra```: Verifica se a entrada contém apenas letras.

- ```URL```: Verifica se a entrada é uma URL válida.

- ```E-mail```: Verifica se a entrada é um endereço de e-mail válido.

- ```Endereço IP```: Verifica se a entrada é um endereço IP válido.

- ```Tempo (24 horas)```: Verifica se a entrada é uma hora válida no formato de 24 horas.

- ```Data (dd/mm/aaaa)```: Verifica se a entrada é uma data válida no formato dd/mm/aaaa.

- ```Telefone```: Verifica se a entrada é um número de telefone válido no formato (DDD)-NNNN-NNNN.

- ```Senha```: Verifica se a entrada é uma senha válida, seguindo critérios específicos.

## Como Usar
1. Selecione o tipo de validação desejado no menu suspenso.
    - A expressão regular correspondente ao tipo selecionado será exibida automaticamente.

2. Insira a entrada que deseja validar no campo "Entrada".
    - Clique no botão "Validar" para ver o resultado da validação.

## Requisitos de Sistema
- Python 3.x
- Tkinter (geralmente incluído na instalação padrão do Python)