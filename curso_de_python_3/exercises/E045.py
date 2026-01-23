"""
E045: Crie um programa que faça o computador jogar Jokenpô com você.
"""

from random import randint

print("""
Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura
""")

jogador = int(input("Qual é a sua jogada? "))
computador = randint(0, 2)

print("-=" * 20)

if computador == 0:
    print("Computador jogou: Pedra")
elif computador == 1:
    print("Computador jogou: Papel")
else:
    print("Computador jogou: Tesoura")

if jogador == 0:
    print("Você jogou: Pedra")
elif jogador == 1:
    print("Você jogou: Papel")
elif jogador == 2:
    print("Você jogou: Tesoura")
else:
    print("Jogada inválida.")

print("-=" * 20)

if jogador == computador:
    print("EMPATE!")
elif jogador == 0 and computador == 2:
    print("VOCÊ VENCEU! Pedra quebra Tesoura.")
elif jogador == 1 and computador == 0:
    print("VOCÊ VENCEU! Papel embrulha Pedra.")
elif jogador == 2 and computador == 1:
    print("VOCÊ VENCEU! Tesoura corta Papel.")
elif jogador in [0, 1, 2]:
    print("VOCÊ PERDEU!")
else:
    print("Não foi possível jogar, escolha inválida.")
