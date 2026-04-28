# Tipos Primitivos e Saída de Dados

Este capítulo aborda a tipagem de dados, a conversão explícita (casting) e métodos avançados de formação de saída e validação de string. 

## Tipos Primitivos Básicos

O Python possui quatro tipos primitivos fundamentais que você utilizará com frequência. Embora a inferência de tipos seja automática na atribuição direta, a entrada de dados via `input()` requer tratamento explícito.

|  | Nome no Python | Descrição |
| --- | --- | --- |
| Inteiro | `int`  | Número inteiros (positivos, negativos ou zero). |
| Ponto Flutuante | `float` | Número reais (com casas decimais). Use **ponto** **`.`** como separador. |
| Booleano | `bool` | Valor lógicos. **Sempre** com inicial maiúscula. |
| String | `str`  | Cadeia de caracteres delimitada por aspas. |

### A Função `type()`

Utilize para verificar o tipo de dado de uma variável ou valor.

```python
n = input('Digite algo: ')
print(type(n))  # Retornará <class 'str'>, pois input sempre retorna string
```

## Conversão de Tipos (Casting)

Como o retorno de `input()` é sempre uma string, é necessário converter explicitamente para realizar operações matemáticas ou lógicas corretas.

### Sintaxe

```python
variavel = tipo_primitivo(valor)
```

**Exemplos Práticos**

```python
# Convertendo para Inteiro (Soma funciona matematicamente)
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro: '))
s = n1 + n2  # Agora é soma, não concatenação

# Convertendo para Real
n_float = float(input('Digite uma nota: '))  # Ex: Digite 4 -> vira 4.0

# Convertendo para Booleano
# Retorna True se houver valor, False se a entrada for vazia (apenas enter)
n_bool = bool(input('Digite algo: '))
```

## Saída Formatada: O Método `.format()`

Uma alternativa mais limpa e moderna à concatenação com vírgula ou `+`. Utiliza máscaras `{}` dentro da string que são substituídas pelos valores passados na função `.format()`.

### Sintaxe

```python
print('Texto {0} texto {1} texto {2}'.format(var1, var2, var3))
# Os índices 0, 1, 2 são opcionais na ordem sequencial
```

## Métodos de Validação de String (`is...`)

Objetos do tipo string (`str`) possuem métodos embutidos para verificar o conteúdo da variável. Retornam sempre `True` ou `False`.

### Principais Métodos

Suponha `n = input("Digite algo: ")`:

- **`n.isnumeric()`**: Retorna `True` se a string puder ser convertida para um número.
- **`n.isalpha()`**: Retorna `True` se conter apenas letras (alfabético).
- **`n.isalnum()`**: Retorna `True` se for alfanumérico (letras e/ou números).
- **`n.isupper()`**: Retorna `True` se estiver tudo em MAIÚSCULAS.
- **`n.islower()`**: Retorna `True` se estiver tudo em minúsculas.
- **`n.isspace()`**: Retorna `True` se conter apenas espaços.

```python
algo = input('Digite algo: ')
print('É numérico?', algo.isnumeric())
print('É alfabético?', algo.isalpha())
print('É alfanumérico?', algo.isalnum())
```

## Desafios

### Exercício 004

Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações possíveis sobre ela. 

```python
text = input("Digite algo: ")
print("O tipo primitivo desse valor é {}".format(type(text)))
print("Só tem espaços? {}".format(text.isspace()))
print("É um número? {}".format(text.isnumeric()))
print("É alfanumérico? {}".format(text.isalnum()))
print("É alfabético? {}".format(text.isalpha()))
print("Está em maiúsculas? {}".format(text.isupper()))
print("Está em minusculas? {}".format(text.islower()))
print("Está capitalizada? {}".format(text.istitle()))
```