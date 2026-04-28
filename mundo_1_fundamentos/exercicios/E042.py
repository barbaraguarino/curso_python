"""
E042: Refaça o Desafio 035 dos triângulos, acrescentando o recuso de mostrar que tipo de triângulo será formado:

- Equilátero: todos os lados iguais.
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
"""

lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print("Os lados formam um triângulo.")

    if lado1 == lado2 == lado3:
        print("Tipo: Triângulo Equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Tipo: Triângulo Isósceles.")
    else:
        print("Tipo: Triângulo Escaleno.")
else:
    print("Os lados NÃO formam um triângulo.")