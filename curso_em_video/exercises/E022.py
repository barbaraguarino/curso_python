"""
E022: Crie um programa que leia o nome completo de uma pessoa e mostre:
    - O nome com todas as letras maiúsculas.
    - O nome com todas as letras minúsculas.
    - Quantas letras ao todo (sem considerar espaços).
    - Quantas letras tem o primeiro nome.
"""

nome_completo = str(input('Digite seu nome completo: ')).strip()
print("Analisando seu nome...")
print(f"Seu nome em maiúsculas é {nome_completo.upper()}")
print(f"Seu nome em minúsculas é {nome_completo.lower()}")
# print(f"Seu nome tem ao todo {len(nome_completo.replace(" ", ""))} letras")
print(f"Seu nome tem ao todo {len(nome_completo) - nome_completo.count(" ")} letras")
primeiro_nome = nome_completo.split()[0]
print(f"Seu primeiro nome é {primeiro_nome.lower().title()} e ele tem {len(primeiro_nome)} letras")