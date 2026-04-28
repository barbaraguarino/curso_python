"""
E027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
"""

nome_completo = str(input("Digite seu nome completo: ")).strip().split()
print("Muito prazer em te conhecer!")
print(f"Seu primeiro nome é {nome_completo[0]}")
print(f"Seu último nome é {nome_completo[-1]}")