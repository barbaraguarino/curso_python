"""
E038: Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- 0 primeiro valor é maior
- 0 segundo valor é maior
- Não existe valor maior, os dois são iguais
"""

first = int(input("Primeiro valor: "))
second = int(input("Segundo valor: "))

if first > second:
    print("O PRIMEIRO valor é maior.")
elif first < second:
    print("O SECUNDO valor é maior.")
else:
    print("Não existe valor maior, os dois são IGUAIS.")