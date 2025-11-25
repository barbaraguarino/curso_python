"""
E015: Escreva um programa que pergunte a quantidade de quilômetros percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por quilômetro rodado.
"""

dias = int(input("Quantos dias alugados? "))
km = float(input("Quando quilômetros rodados? "))

print("O total a pagar é de R${:.2f}.".format(dias*60 + km*0.15))