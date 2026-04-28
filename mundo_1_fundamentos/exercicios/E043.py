"""
E043: Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida
"""

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura ** 2)

print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Status: Abaixo do Peso")
elif imc < 25:
    print("Status: Peso ideal")
elif imc < 30:
    print("Status: Sobrepeso")
elif imc < 40:
    print("Status: Obesidade")
else:
    print("Status: Obesidade mórbida")
