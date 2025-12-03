"""
E018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
"""

from math import sin, cos, tan, radians

angle = float(input("Digite o ângulo que você deseja: "))

print(f"O ângulo de {angle:.2f} tem o SENO de {sin(radians(angle)):.2f}")
print(f"O ângulo de {angle:.2f} tem o COSSENO de {cos(radians(angle)):.2f}")
print(f"O ângulo de {angle:.2f} tem o TANGENTE de {tan(radians(angle)):.2f}")