# Condições (Parte 1): Estruturas de Controle

Até o momento, todos os algoritmos estudados seguiam uma **Estrutura Sequencial**, onde os comandos são executados rigorosamente de cima para baixo, um após o outro, sem desvios. A partir desde ponto, introduzimos as **Estruturas Condicionais**, que permitem ao programa “tomar decisões” baseadas em testes lógicos, bifurcando o fluxo de execução.

## O Conceito de Indentação e Blocos

Diferente de linguagens como C, Java ou PHP, que utilizam chaves `{}` para delimitar blocos de código, o Python utiliza a **indentação** (recuo visual).

- **Indentação Obrigatória:** Todo código subordinado a uma condição (o que acontece dentro do `if` ou `else`) deve estar recuado à direita (geralmente 4 espaços ou 1 TAB).
- **Hierarquia:** O Python sabe onde um bloco termina quando a indentação volta ao nível anterior (à esquerda).

## Estrutura Condicional Simples: `if`

Ocorre quando o programa testa uma condição e executa um bloco de código **apenas se ela for verdadeira**. Se for `false`, o programa simplesmente segue adiante sem fazer nada específico para o erro:

**Sintaxe:**

```python
if condicao:
    bloco_verdadeiro
```

**Exemplo Prático:**

```python
nome = input('Qual é seu nome? ')
if nome == 'Gustavo':
    print('Que nome lindo você tem!') # Só executa se nome for Gustavo
print('Bom dia, {}!'.format(nome)) # Executa SEMPRE (está fora do bloco)
```

## Estrutura Condicional Composta: `if-else`

Ocorre quando definimos dois caminhos distintos: um para caso a condição seja **verdadeira** e outro para caso seja **falsa**. Nunca ambos os blocos serão executados na mesma rodada.

**Sintaxe:**

```python
if condicao:
    bloco_verdadeiro
else:
    bloco_falso
```

***Atenção:** Os dois pontos `:` no final das linhas do `if` e do `else` são **obrigatórios**.*

**Exemplo Prático:**

```python
tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')
print('--FIM--')
```

## Condição Simplificada (Ternária): `if...else`

Para situações muito simples, o Python permite escrever a estrutura `if...else` em uma única linha. É equivalente ao operador ternário de outras linguagens.

**Sintaxe:**

```python
comando_se_verdadeiro if condicao else comando_se_falso
```

**Exemplo Prático:** 

```python
media = 7.5
print('Parabéns' if media >= 6 else 'Estude mais')
```

*Embora conciso, o uso excessivo pode prejudicar a legibilidade do código.*

## Exercícios

### Exercícios 28

Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 a 5 e paça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.

```python
from time import sleep
from random import randint

print("-=-" * 20)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("-=-" * 20)

num = randint(0,5)

palpite = int(input("Em que número eu pensei? "))

print("PROCESSANDO...")
sleep(2)

if num == palpite:
    print(f"VOCÊ GANHOU!!! Eu pensei no número {num}.")
else:
    print(f"GANHEI! Eu pensei no número {num} e não no {palpite}!")
```

### Exercícios 29

Escreva um programa que leia a velocidade de um carro.

Se ela ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.

A multa vai custar R$7,00 por cada Km acima do limite.

```python
velocidade = float(input('Qual a velocidade atual? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite.')
    multa = (velocidade - 80) * 7
    print('Valor da multa: R${:.2f}'.format(multa))
print('Dirija com segurança!')
```

### Exercícios 30

Crie um programa que leia o número inteiro e mostre na tela se ela é PAR ou ÍMPAR.

```python
numero = int(input('Digite um número: '))
if numero % 2 == 0:
    print('O número é PAR')
else:
    print('O número é ÍMPAR')
```

### Exercícios 31

Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200km e R$0,45 para viagens mais longas.

```python
distancia = float(input('Distância da viagem em Km: '))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('O preço da sua passagem será R${:.2f}'.format(preco))
```

### Exercícios 32

Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO. 

```python
from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO')
else:
    print(f'O ano {ano} NÃO é BISSEXTO')
```

### Exercícios 33

Faça um programa que leia três números e mostre qual é o **maior** e qual é o **menor**. 

```python
a = int(input('Valor 1: '))
b = int(input('Valor 2: '))
c = int(input('Valor 3: '))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
    
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'Menor: {menor} | Maior: {maior}')
```

### Exercícios 34

Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.

Para salários superiores a R$1.250,00, calcule um aumento de 10%.

Para os inferiores ou iguais, o aumento é de 15%.

```python
salario = float(input('Salário atual: R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(salario, novo))
```

### Exercícios 35

Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou terem formado um triângulo.

```python
r1 = float(input('Segmento 1: '))
r2 = float(input('Segmento 2: '))
r3 = float(input('Segmento 3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos PODEM FORMAR um triângulo!')
else:
    print('Os segmentos NÃO PODEM FORMAR um triângulo!')
```