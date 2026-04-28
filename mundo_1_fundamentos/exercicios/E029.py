"""
E029: Escreva um programa que leia a velocidade de um carro.
    - Se ela ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
    - A multa vai custar R$7,00 por cada Km acima do limite.
"""

velocidade = float(input('Qual a velocidade atual? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite.')
    multa = (velocidade - 80) * 7
    print('Valor da multa: R${:.2f}'.format(multa))
print('Dirija com segurança!')