"""
E005: Faça um programa que leia um número
Inteiro e mostre na tela o seu sucessor e seu antecessor.
"""

num = int(input("Digite um número: "))
print("Analisando o valor {}; seu antecessor é {} e o sucessor é {}".format(num, num-1, num+1))