"""
E028: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 a 5 e paça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""
from time import sleep
from random import randint

print("-=-" * 20)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("-=-" * 20)

num = randint(0,5)

palpite = int(input("Em que número eu pensei? "))

print("PROCESSANDO...")
sleep(2)

if num == palpite:
    print(f"VOCÊ GANHOU!!! Eu pensei no número {num}.")
else:
    print(f"GANHEI! Eu pensei no número {num} e não no {palpite}!")