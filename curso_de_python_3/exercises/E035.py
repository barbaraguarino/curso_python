"""
E035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou terem formado um triângulo.
"""

r1 = float(input('Segmento 1: '))
r2 = float(input('Segmento 2: '))
r3 = float(input('Segmento 3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos PODEM FORMAR um triângulo!')
else:
    print('Os segmentos NÃO PODEM FORMAR um triângulo!')