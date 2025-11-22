"""
E007: Desenvolva um programa que leia as duas notas de um aluno,
calcule e mostre sua média.
"""

num1 = float(input("Primeira nota do aluno: "))
num2 = float(input("Segunda nota do aluno: "))
print("A média entre {:.2f} e {:.2f} é igual a {:.2f}".format(num1, num2, (num1+num2)/2))