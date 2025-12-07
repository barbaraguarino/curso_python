"""
E033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""

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