"""
E011: Faça um programa que leia a largura e a altura de uma parede
em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta pinta uma área de $2m^2$.
"""

largura = float(input("Qual a largura da parede em metros: "))
altura = float(input("Qual a altura da parede em metros: "))

print("Sua parede tem dimensão de {:.2f}x{:.2f} metros e sua área é de {:.2f}m².".format(largura, altura, largura*altura))
print("Para pintar essa parede, você precisará de {:.2f}l de tinta.".format((largura*altura)/2))