"""
E009: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
"""

num = int(input("Digite um número para ver sua tabuada: "))

print()
i = 1
for i in range(1, 11):
    print("{} x {:2} = {:2}".format(num, i, num*i))