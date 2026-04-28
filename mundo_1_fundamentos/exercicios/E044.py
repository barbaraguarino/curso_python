"""
E044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

- À vista dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
"""

preco = float(input("Preço do produto: R$ "))

print("""
FORMAS DE PAGAMENTO
[1] À vista dinheiro/cheque
[2] À vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
""")

opcao = int(input("Escolha a forma de pagamento: "))

if opcao == 1:
    valor_final = preco * 0.90
    print(f"Pagamento à vista no dinheiro/cheque.")
    print(f"Desconto de 10% aplicado.")
    print(f"Valor a pagar: R$ {valor_final:.2f}")

elif opcao == 2:
    valor_final = preco * 0.95
    print(f"Pagamento à vista no cartão.")
    print(f"Desconto de 5% aplicado.")
    print(f"Valor a pagar: R$ {valor_final:.2f}")

elif opcao == 3:
    valor_final = preco
    parcela = valor_final / 2
    print(f"Pagamento em 2x no cartão.")
    print(f"2 parcelas de R$ {parcela:.2f}")
    print(f"Valor total: R$ {valor_final:.2f}")

elif opcao == 4:
    parcelas = int(input("Número de parcelas: "))
    valor_final = preco * 1.20
    parcela = valor_final / parcelas
    print(f"Pagamento em {parcelas}x no cartão.")
    print(f"Juros de 20% aplicados.")
    print(f"{parcelas} parcelas de R$ {parcela:.2f}")
    print(f"Valor total: R$ {valor_final:.2f}")

else:
    print("Opção de pagamento inválida.")