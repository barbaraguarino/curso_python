"""
E012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""

valor = float(input("Qual é o preço do produto? R$"))
print("O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}".format(valor,valor-(valor*(5/100))))