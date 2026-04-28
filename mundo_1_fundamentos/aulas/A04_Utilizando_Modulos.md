# Utilizando Módulos

Até agora, utilizamos apenas as funcionalidades “de fábrica” (built-in) do Python. Para expandir as capacidades da linguagem — como realizar cálculos matemáticos avançados, gerar números aleatórios ou interagir com o sistema operacional — utilizamos **módulos**. 

Um módulo é, essencialmente, um arquivo contendo definições e instruções Python que podem ser importados para outros programas. 

## Importando Bibliotecas (O Comando `import`)

Existem duas formas principais de importar módulos em Python, cada uma com implicações diferentes no uso de memória e na sintaxe do código.

### Importação Generalista (`import`)

Carregada **todas** as funcionalidades de módulo para memória. Para usar uma função, é necessário referenciar o módulo (`modulo.funcao()`).

**Sintaxe:**

```python
import nome_do_modulo
```

**Exemplo com biblioteca** `math`:

```python
import math

num = int(input("Digite um número: "))
raiz = math.sqrt(num)  # Necessário usar o prefixo 'math.'
print(f"A raiz de {num} é {raiz}")
```

### Importação Específica (`from ... import`)

Carregada **apenas** as funcionalidades selecionadas, economizando memória. Não é necessário usar o prefixo do módulo para chamar a função.

**Sintaxe:**

```python
from nome_do_modulo import funcao1, funcao2
```

**Exemplo Otimizado:**

```python
from math import sqrt, floor

num = int(input("Digite um número: "))
raiz = sqrt(num)        # Uso direto, sem 'math.'
print(f"A raiz arredondada para baixo é {floor(raiz)}")
```

## A Biblioteca Padrão: `math`

O módulo `math` fornece funções matemáticas definidas pelo padrão C. Abaixo, as principais funções apresentadas:

| **Função** | **Descrição** | **Exemplo de Uso** |
| --- | --- | --- |
| `ceil(x)` | Arredonda `x` para cima (teto). | `math.ceil(4.2)` $\to$ `5` |
| `floor(x)` | Arredonda `x` para baixo (chão). | `math.floor(4.9)` $\to$ `4` |
| `trunc(x)` | Elimina a parte decimal de `x` sem arredondar. | `math.trunc(4.9)` $\to$ `4` |
| `pow(x, y)` | Potência ($x^y$). Similar a `x**y`. | `math.pow(5, 2)` $\to$ `25.0` |
| `sqrt(x)` | Raiz quadrada de `x`. | `math.sqrt(81)` $\to$ `9.0` |
| `factorial(n)` | Retorna o fatorial de `n`. | `math.factorial(5)` $\to$ `120` |

## Números Aleatórios: Módulo `random`

Para gerar "números aleatórios" (pseudo-aleatórios), utilizamos o módulo `random`.

**Exemplos Práticos:**

```python
import random

# Gera um float aleatório entre 0 e 1
num_float = random.random()

# Gera um inteiro aleatório entre 1 e 10 (inclusivo)
num_int = random.randint(1, 10)

print(f"Float: {num_float:.2f} | Inteiro: {num_int}")
```

## PyPI e Instalação de Pacotes Externos

Além das bibliotecas padrão (Standard Library), o Python possui um vasto repositório de pacotes de terceiros chamado **PyPI (Python Package Index)**.

### Instalação via PyCharm

O vídeo demonstra como instalar pacotes (como a biblioteca `emoji`) diretamente pela IDE PyCharm:

1. Vá em **File > Settings** (ou Preferences no Mac).
2. Navegue até **Project: [nome_projeto] > Python Interpreter**.
3. Clique no ícone **+** (Install).
4. Pesquise pelo pacote desejado (ex: `emoji`) e clique em **Install Package**.

### Exemplo com Pacote Externo (`emoji`)

```python
import emoji

print(emoji.emojize("Olá, Mundo :earth_americas:", language='alias'))
# Saída: Olá, Mundo 🌎
```

***Nota*:** A sintaxe da biblioteca `emoji` pode mudar entre versões. Sempre consulte a documentação oficial do pacote no PyPI.

## Exercícios

### Exercício 16

Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.

```python
from math import trunc

num = float(input("Digite um valor: "))
print(f"O valor digitado foi {num} e a sua porção inteira é {trunc(num)}.")
```

### Exercício 17

Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa. 

```python
from math import hypot

cateto_oposto = float(input("Comprimento do cateto oposto: "))
cateto_adjacente = float(input("Comprimento do cateto adjacente: "))
print(f"A hipotenusa vai medir {hypot(cateto_oposto, cateto_adjacente):.2f}")
```

### Exercício 18

Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo. 

```python
from math import sin, cos, tan, radians

angle = float(input("Digite o ângulo que você deseja: "))

print(f"O ângulo de {angle:.2f} tem o SENO de {sin(radians(angle)):.2f}")
print(f"O ângulo de {angle:.2f} tem o COSSENO de {cos(radians(angle)):.2f}")
print(f"O ângulo de {angle:.2f} tem o TANGENTE de {tan(radians(angle)):.2f}")
```

### Exercício 19

Um professor quer sortear um dos seus quatros alunos para apagar o quadro. Faça um programa que ajude ela, lendo o nome deles e escrevendo o nome do escolhido.

```python
from random import choice

alunos = []

print("Digite os nomes dos alunos, quando quiser parar der enter.\n")

while True:
    aluno = input("Digite o nome do aluno: ")
    if aluno != "":
        alunos.append(aluno)
    else:
        break

print("O aluno escolhido foi: {}".format(choice(alunos)))
```

### Exercício 20

O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatros alunos e mostre a ordem sorteada.

```python
print("Informe os nomes dos alunos e quando terminar der enter.")

alunos = []

while True:
    aluno = input("Digite o nome do aluno: ")
    if aluno != "":
        alunos.append(aluno)
    else:
        break

alunos.sort()
ii = 1

print("\nOrdem da apresentação:")
for aluno in alunos:
    print(f"{ii}: {aluno}")
    ii += 1
```