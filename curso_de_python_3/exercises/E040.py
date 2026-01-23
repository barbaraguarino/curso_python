"""
E040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

- Média abaixo de 5.0: Reprovado
- Média entre 5.0 e 6.9: Recuperação
- Média 7.0 ou superior: Aprovado
"""

first = float(input("Primeira nota: "))
second = float(input("Segunda nota: "))

media = (first + second) / 2

print(f"Tirando {first:.2f} e {second:.2f}, a média do aluno é {media:.2f}.")

if media >= 7.0:
    print("O aluno está APROVADO.")
elif media < 5.0:
    print("O aluno está REPROVADO.")
elif 5.0 <= media < 7.0:
    print("O aluno está de RECUPERAÇÃO.")
