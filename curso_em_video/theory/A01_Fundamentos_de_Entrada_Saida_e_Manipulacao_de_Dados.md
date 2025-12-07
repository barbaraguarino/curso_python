## Introdução

Este capítulo aborda as primitivas fundamentais para integração com o usuário via terminal, declaração de variáveis e a natureza da tipagem dinâmica no Python em operações básicas.

## Saída de Dados: Função `print()`

Responsável por enviar informações para a saída padrão (stdout).

### Sintaxe e Delimitadores

- **String: ****Devem ser delimitadas por aspas simples (`'...'`) ou duplas (`"..."`).
- **Números:** Devem ser passados sem aspas para serem interpretados como valores numéricos.

### Concatenação e Junção

O Python oferece formas distintas de unir valores dentro do `print()`:

1. **Operador** `+` **(Concatenação Estrita):**
    1. Une strings sem adicionar espaços.
    2. **Restrição:** Só funciona se ambos os operandos forem strings. Tentar somar `str + int` gera `TypeError`.
2. **Separador `,` (Junção com Espaço):**
    1. Imprime múltiplos argumentos separados por um espaço padrão.
    2. **Vantagem:** Aceita tipos mistos (ex: string e número) na mesma chamada.

```python
# Exemplo 01: Diferença entre Vírgula e Mais
print('Olá', 5)    # Saída: Olá 5 (Aceita tipos mistos)
# print('Olá' + 5) # ERRO: TypeError (Não concatena str com int)
print('Olá' + '5') # Saída: Olá5 (Concatenação de strings)
```

## Variáveis e Atribuição

Variáveis são identificadores que referenciam espaços na memória. Em Python, **toda variável é um objeto**.

- **Operador de Atribuição (`=`):** Lê-se “receber”. Atribui o valor à direita ao identificador à esquerda.
- **Tipagem Dinâmica:** O tipo de variável é definido pelo valor atribuído no momento da execução.

```python
# Exemplo 02: Atribuição de Variáveis
nome = 'Guanabara'  # Tipo str
idade = 25          # Tipo int
peso = 75.8         # Tipo float

print(nome, idade, peso)
```

## Entrada de Dados: Função `input()`

Responsável por ler dados de entrada padrão (teclado).

### Sintaxe

```python
variavel = input('Mensagem de prompt: ')
```

### Comportamento Crítico (Tipagem)

A função `input()` **sempre retorna uma string (str)**, independentemente do que o usuário digitar (letras ou números).

- Isso implica que operações aritméticas diretas sobre o retorno de `input()` resultarão em **concatenação**, não em cálculo matemático.

## O Problema da Soma vs. Concatenação

Um erro comum ao iniciar em Python é tentar somar valores capturados diretamente pelo `input()`.

| **Expressão** | **Tipos dos Operadores** | Operação | Resultado |
| --- | --- | --- | --- |
| `7 + 4` | `int` + `int`  | Soma Aritmética | `11` |
| `'7' + '4'` | `str` + `str` | Concatenação | `'74'` |

**Nota de Revisão:** Para realizar cálculos matemáticos com entrada do usuário, é necessário converter o tipo de dado (*casting*) usando `int()` ou `float()`. *Este conceito é introduzido na aula seguinte (Tipo Primitivos), mas é essencial ter em mente agora*.

## Modos de Execução

O vídeo destaca a diferença entre testar e desenvolver:

- **Modo Interativo (Python Shell/IDLE)**:
    - Execução linha a linha.
    - Ideal para testes rápidos e verificação de comportamento de funções.
    - Não salva o código.
- **Modo Script (Arquivos** `.py`):
    - Código escrito em um arquivo de texto e salvo.
    - Execução em lote (todas as linhas sequencialmente).
    - Ideal para criar programas complexos e reutilizáveis.

## Desafios Práticos

### Exercício 001

Crie um script em Python que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas de acordo com o valor digitado.

```python
nome = input("Qual é o seu nome? ")
print("Olá", nome + "! Prazer em te conhecer!")

'''
Qual é o seu nome? [Nome]
Olá [Nome]! Prazer em te conhecer!
'''
```

### Exercício 002

Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada.

```python
day = input("Dia = ")
month = input("Mês = ")
year = input("Ano = ")

print("Você nasceu em", day + "/" + month + "/" + year + ". Correto?")

'''
Dia = [Dia]
Mês = [Mês]
Ano = [Ano]
Você nasceu em [data]/[Mês]/[Ano]. Correto?
'''
```

### Exercício 003

Crie um script Python que leia dois números e tenta mostrar a soma ente eles.

```python
num1 = input("Primeiro número: ")
num2 = input("Segundo número: ")

print("A soma é" ,num1 + num2)

soma = int(num1) + int(num2)

print("Na verdade, a soma correta é", soma)

'''
Primerio número: [Num1] 
Segundo número: [Num2]
A soma é [Num1Num2]
'''-
```