"""
EX004: Faça um programa que leia algo pelo teclado e mostre na tela o seu
tipo primitivo e todas as informações possíveis sobre ela.
"""

text = input("Digite algo: ")
print("O tipo primitivo desse valor é {}".format(type(text)))
print("Só tem espaços? {}".format(text.isspace()))
print("É um número? {}".format(text.isnumeric()))
print("É alfanumérico? {}".format(text.isalnum()))
print("É alfabético? {}".format(text.isalpha()))
print("Está em maiúsculas? {}".format(text.isupper()))
print("Está em minusculas? {}".format(text.islower()))
print("Está capitalizada? {}".format(text.istitle()))