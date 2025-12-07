## Introdução

Este capítulo aborda a capacidade matemática nativa do Python, fundamental para processamento de dados, cálculos científicos e lógica de programação.

## Operadores Binários

Diferente de matemática tradicional que usa símbolos como `x` ou `-`, o Python adota uma sintaxe específica, herdada de linguagens como C e Java.

| Símbolo | Operação |
| --- | --- |
| `+`  | Adição |
| `-` | Subtração |
| `*` | Multiplicação |
| `/` | Divisão Real |
| `**` | Porência |
| `//` | Divisão Inteira |
| `%` | Módulo |

### Notas Importantes

1. **Divisão Inteira (`//`) vs Real (`/`):** A divisão real resulta em um resultado `float` e a divisão inteira resulta em um resultado `int`.
2. **Potência (`**`):** Para calcular raízes, utiliza-se as potência inversa que seria `81 ** (1/2)` ou utilizar a função interna `pow(base, exp)`.

## Ordem de Precedência

O Python não executa operações apenas da esquerda para a direita; ele segue uma hierarquia estrita. Ignorar isso é a causa número um de erros lógicos em cálculos.

1. **`()` Parênteses:** Têm a maior prioridade. Usados para forçar a execução de blocos específicos.
2. **`*` Potenciação:** Executada antes de multiplicações ou divisões.
3. **, `/`, `//`, `%`:** Multiplicação, Divisão, Divisão Inteira e Módulo. (Se aparecerem juntos, executa-se quem vier primeiro, da esquerda para a direita).
4. **`+`, :** Soma e Subtração (Menor prioridade).

**Exemplo de Precedência**

```python
# Expressão: 3 * 5 + 4 ** 2
# 1. Potência: 4 ** 2 = 16
# 2. Multiplicação: 3 * 5 = 15
# 3. Soma: 15 + 16 = 31
resultado = 3 * 5 + 4 ** 2  # 31

# Alterando com parênteses
# 1. Soma: (5 + 4) = 9
# 2. Potência: 9 ** 2 = 81
# 3. Multiplicação: 3 * 81 = 243
resultado_parenteses = 3 * (5 + 4) ** 2 # 243
```

## Manipulação de String com Operadores

Alguns operadores aritméticos possuem comportamento polimórfico (diferente) quando aplicados a Strings.

- **Concatenação (`+`):** Junta strings.
- **Replicação ():** Repete a string N vezes.

```python
print('Oi' + 'Olá')  # Saída: OiOlá
print('Oi' * 5)      # Saída: OiOiOiOiOi
print('=' * 20)      # Saída: ==================== (Útil para menus)
```

## Formatação Avançada no `print`

Aprofundando o uso do `.format()`, podemos especificar largura de campo e alinhamento.

### Sintaxe

```python
 {:<alinhamento><largura>}
```

- `>` : Alinhado à Direita.
- `<` : Alinhado à Esquerda.
- `^` : Centralizado.
- `:=^20` : Centralizado em 20 espaços, preenchendo o vazio com `=`.

```python
nome = input('Qual seu nome? ')
print('Prazer em te conhecer {:=^20}!'.format(nome))
# Se nome for "Ana", saída: Prazer em te conhecer ========Ana=========!
```

### Controle de Linha (`end` e `\n`)

- `\n`: Caractere de escape para **quebrar** linha (Nova Linha).
- `end=''`: Parâmetro do `print` para **não quebrar** a linha ao final. O padrão é `end='\n'`.

```python
print('Curso em', end=' ')
print('Vídeo')
# Saída: Curso em Vídeo (na mesma linha)
```

## Exercícios

### Exercício 005

Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

```python
num = int(input("Digite um número: "))
print("Analisando o valor {}; seu antecessor é {} e o sucessor é {}".format(num, num-1, num+1))
```

### Exercício 006

Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

```python
num = int(input("Digite um número: "))
print("O dobro de {} vale {}".format(num, num*2))
print("O triplo de {} vale {}".format(num, num*3))
print("O raiz quadrada de {} é igual a {:.2f}".format(num, num**(1/2)))
```

### Exercício 007

Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.

```python
num1 = float(input("Primeira nota do aluno: "))
num2 = float(input("Segunda nota do aluno: "))
print("A média entre {:.2f} e {:.2f} é igual a {:.2f}".format(num1, num2, (num1+num2)/2))
```

### Exercício 008

Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milímetros.

```python
medida = float(input("Uma distância em metros: "))
print("A médida de {:.2f}m corresponde a:".format(medida))
print("KM: {:.3f}".format(medida/1000))
print("HM: {:.2f}".format(medida/100))
print("DAM: {:.1f}".format(medida/10))
print("DM: {:.1f}".format(medida*10))
print("CM: {:.1f}".format(medida*100))
print("MM: {:.1f}".format(medida*1000))
```

### Exercício 009

Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

```python
num = int(input("Digite um número para ver sua tabuada: "))

print()
i = 1
for i in range(1, 11):
    print("{} x {:2} = {:2}".format(num, i, num*i))
```

### Exercício 010

Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. Considere US$ 1.00 = R$ 3.27. 

```python
dinheiro = float(input("Quando dinheiro você tem na carteira? R$"))
print("Com R${:.2f} você pode comprar US${:.2f}".format(dinheiro,dinheiro/3.27))
```

### Exercício 011

Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de $2m^2$.

```python
largura = float(input("Qual a largura da parede em metros: "))
altura = float(input("Qual a altura da parede em metros: "))

print("Sua parede tem dimensão de {:.2f}x{:.2f} metros e sua área é de {:.2f}m².".format(largura, altura, largura*altura))
print("Para pintar essa parede, você precisará de {:.2f}l de tinta.".format((largura*altura)/2))
```

### Exercício 012

Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

```python
valor = float(input("Qual é o preço do produto? R$"))
print("O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}".format(valor,valor-(valor*(5/100))))
```

### Exercício 013

Faça um algoritmo que leia o solário de um funcionário e mostre seu novo salário, com 15% de aumento.

```python
salario = float(input("Qual é o salário do Funcionário? R$"))
print("Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}.".format(salario, salario+(salario*(15/100))))
```