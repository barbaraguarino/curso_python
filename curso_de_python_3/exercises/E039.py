"""
E039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

- Se ele ainda vai ser alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou do tempo do alistamento

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""

from datetime import date

ano = int(input("Digite o ano de nascimento: "))
idade = date.today().year - ano

print(f"Quem nasceu em {ano} tem {idade} anos em {date.today().year}.")

if idade < 18:
    print(f"Ainda faltam {18 - idade} para o alistamento.")
    print(f"Seu alistamento será em {date.today().year + (18 - idade)}.")
elif idade == 18:
    print("Você tem que se alistar IMEDIATAMENTE.")
else:
    print(f"Você já deveria tr se alistado há {idade - 18} anos.")
    print(f"Seu alistamento foi em {date.today().year - (idade - 18)}.")