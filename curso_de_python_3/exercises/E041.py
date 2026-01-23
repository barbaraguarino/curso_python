"""
E041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

- Até 9 anos: Mirim
- Até 14 anos: Infantil
- Até 19 anos: Junior
- Até 20 anos: Sénior
- Acima: Master
"""

from datetime import date

ano = int(input("Digite o ano de nascimento do atleta: "))
idade = date.today().year - ano

print("O atleta tem {} anos.".format(idade))
if idade <= 9:
    print("Classificação: MIRIM")
elif idade <= 14:
    print("Classificação: INFANTIL")
elif idade <= 19:
    print("Classificação: JUNIOR")
elif idade <= 20:
    print("Classificação: SÉNIOR")
else:
    print("Classificação: MASTER")