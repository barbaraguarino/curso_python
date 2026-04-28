"""
E019: Um professor quer sortear um dos seus quatros alunos para apagar o quadro. Faça um programa que ajude ela, lendo o nome deles e escrevendo o nome do escolhido.
"""

from random import choice

alunos = []

print("Digite os nomes dos alunos, quando quiser parar der enter.\n")

while True:
    aluno = input("Digite o nome do aluno: ")
    if aluno != "":
        alunos.append(aluno)
    else:
        break

print("O aluno escolhido foi: {}".format(choice(alunos)))

