"""
E020: O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatros alunos e mostre a ordem sorteada.
"""

print("Informe os nomes dos alunos e quando terminar der enter.")

alunos = []

while True:
    aluno = input("Digite o nome do aluno: ")
    if aluno != "":
        alunos.append(aluno)
    else:
        break

alunos.sort()
ii = 1

print("\nOrdem da apresentação:")
for aluno in alunos:
    print(f"{ii}: {aluno}")
    ii += 1