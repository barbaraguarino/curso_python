## Introdução

Em Python, todo texto é tratado como uma **Cadeira de Caracteres** (`strings`). 

Tecnicamente, ao atribuir uma string a uma variável, o Python aloca cada caractere (incluindo espaços) em um índice sequencial na memória, começando sempre do índice **0**.

```python
# Exemplo de alocação na memória para "Curso em Video"
# [C][u][r][s][o][ ][e][m][ ][V][i][d][e][o]
#  0  1  2  3  4  5  6  7  8  9 10 11 12 13
```

## Fatiamento de String (Slicing)

Permite extrair pedaços da string usando a notação `[início:fim:passo]`. *Lembre-se: O índice final é sempre exclusivo (o Python para um antes).*

| **Sintaxe** | **Descrição** | **Exemplo (frase = 'Curso em Video')** | **Resultado** |
| --- | --- | --- | --- |
| `[9]` | Pega apenas o caractere no índice 9. | `frase[9]` | `'V'` |
| `[9:13]` | Do índice 9 até o 12 (exclui o 13). | `frase[9:13]` | `'Vide'` |
| `[9:21]` | Do 9 até o 20 (ou final se exceder). | `frase[9:21]` | `'Video'` |
| `[9:21:2]` | Do 9 até o 21, pulando de 2 em 2. | `frase[9:21:2]` | `'Vdo'` |
| `[:5]` | Do início (implícito 0) até o 4. | `frase[:5]` | `'Curso'` |
| `[15:]` | Do 15 até o final da string. | `frase[15:]` | *(última palavra)* |
| `[9::3]` | Começa no 9, vai até o fim, pulando de 3 em 3. | `frase[9::3]` | `'Ve'` |

## Análise de String

Métodos para extrair informações sobre o conteúdo da string.

- **`len(frase)`**: Retorna o **comprimento** (quantidade de caracteres) da string.
    - Ex: `len('Curso')` → `5`
- **`frase.count('o')`**: Conta quantas vezes o caractere `'o'` (minúsculo) aparece.
    - *Variação:* `frase.count('o', 0, 13)` → Conta ocorrências apenas no fatiamento do índice 0 ao 12.
- **`frase.find('deo')`**: Procura a sequência `'deo'` e retorna o **índice** onde ela começa.
    - Se retornar `1`, significa que a string **não existe**.
- **Operador `in`**: Verifica se uma palavra existe na string. Retorna `True` ou `False`.
    - Ex: `'Curso' in frase` → `True`

## Transformação de Strings

Métodos que alteram a formatação. **Atenção:** Como strings são imutáveis, estes métodos **retornam uma nova string**, eles não alteram a original a menos que você faça uma nova atribuição (`frase = frase.replace(...)`).

- **`frase.replace('Python', 'Android')`**: Substitui a primeira palavra pela segunda.
- **`frase.upper()`**: Transforma tudo para **MAIÚSCULAS**.
- **`frase.lower()`**: Transforma tudo para **minúsculas**.
- **`frase.capitalize()`**: Deixa apenas o **primeiro caractere** da string maiúsculo; o resto vira minúsculo.
- **`frase.title()`**: Analisa a string e coloca a **primeira letra de cada palavra** em maiúscula (baseado nos espaços).
- **`frase.strip()`**: Remove todos os **espaços inúteis** no início e no final da string.
    - `frase.rstrip()`: Remove espaços apenas da direita (Right).
    - `frase.lstrip()`: Remove espaços apenas da esquerda (Left).

## Divisão e Junção

### Divisão (`split`)

**`frase.split()`**: Divide a string inteira em uma **lista** (vetor), usando os espaços como separador padrão.

- Ex: `'Curso em Video'.split()` → `['Curso', 'em', 'Video']`
- Cada palavra recebe um novo índice independente dentro da lista.

### Junção (`join`)

**`'-'.join(lista)`**: Junta os elementos de uma lista em uma única string, usando o caractere definido (neste caso, hífen) como separador.

- Ex: `'-'.join(['Curso', 'em', 'Video'])` → `'Curso-em-Video'`

## Dica Pro: Strings de Múltiplas Linhas

Para armazenar textos longos que ocupam várias linhas (como menus ou docstrings) sem usar vários `print()`, utilize **três aspas** (simples ou duplas).

```python
print("""
     Bem-vindo ao sistema!
     Escolha uma opção:
     1 - Cadastro
     2 - Sair
""")
```

## Exercícios

### Exercício 22

Crie um programa que leia o nome completo de uma pessoa e mostre:

- O nome com todas as letras maiúsculas.
- O nome com todas as letras minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.

```python
nome_completo = str(input('Digite seu nome completo: ')).strip()
print("Analisando seu nome...")
print(f"Seu nome em maiúsculas é {nome_completo.upper()}")
print(f"Seu nome em minúsculas é {nome_completo.lower()}")
# print(f"Seu nome tem ao todo {len(nome_completo.replace(" ", ""))} letras")
print(f"Seu nome tem ao todo {len(nome_completo) - nome_completo.count(" ")} letras")
primeiro_nome = nome_completo.split()[0]
print(f"Seu primeiro nome é {primeiro_nome.lower().title()} e ele tem {len(primeiro_nome)} letras")
```

### Exercício 23

Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

```python
num = int(input("Informe um número: "))
print("Analisando o número {}".format(num))
print(f"Unidade: {num // 1 % 10}")
print(f"Dezena: {num // 10 % 10}")
print(f"Centena: {num // 100 % 10}")
print(f"Milhar: {num // 1000 % 10}")
```

### Exercício 24

Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome “SANTO”. 

```python
cidade = str(input("Em que cidade você nasceu? ")).strip()
print(cidade[:5].lower() == "santo")
```

### Exercício 25

Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

```python
nome_completo = str(input("Qual o seu nome completo? "))
print(f"Seu nome completo tem Silva? {nome_completo.lower().count("silva")>0}")
```

### Exercício 26

Faça um programa que leia uma frase pelo teclado e mostre:

- Quantas vezes aparece a letra “A”.
- Em que posição ela aparece a primeira vez.
- Em que posição ela aparece a última vez.

```python
frase = str(input("Digite uma frase: ")).strip().upper()
print("Analisando a frase...")
print(f"A letra A aparece {frase.count('A')} vezes na frase.")
print(f"A primeira letra A apareceu na posição {frase.find('A')+1}.")
print(f"A última letra A apareceu na posição {frase.rfind('A')+1}.")
```

### Exercício 27

Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

```python
nome_completo = str(input("Digite seu nome completo: ")).strip().split()
print("Muito prazer em te conhecer!")
print(f"Seu primeiro nome é {nome_completo[0]}")
print(f"Seu último nome é {nome_completo[-1]}")
```