"""
E014: Escreva um programa que converta uma temperatura digitada em °C e converta para °F.
"""

temperatura = float(input("Informe a temperatura em °C: "))
print("A temperatura de {:.2f}°C corresponde a {:.2f}°F".format(temperatura, temperatura*1.8+32))