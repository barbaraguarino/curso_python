"""
E036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
"""

valor = float(input("Valor da casa: R$"))
salario = float(input("Salário do comprador: R$"))
anos = int(input("Quantos anos de financiamento? "))

prestacao = valor / (anos*12)

print(f"Para pagar uma casa de R${valor:.2f} em {anos} anos a prestação será de R${prestacao:.2f} por mês.")

if prestacao > (salario * 30 / 100):
    print("Empréstimo NEGADO!")
else:
    print("Empréstimo APROVADO!")