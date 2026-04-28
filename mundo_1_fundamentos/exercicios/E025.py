"""
E025: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
"""

nome_completo = str(input("Qual o seu nome completo? "))
print(f"Seu nome completo tem Silva? {nome_completo.lower().count("silva")>0}")