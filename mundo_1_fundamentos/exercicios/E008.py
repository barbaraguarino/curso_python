"""
E008: Escreve um programa que leia um valor em metros e exiba convertido em
centímetros e milímetros.
"""

medida = float(input("Uma distância em metros: "))
print("A médida de {:.2f}m corresponde a:".format(medida))
print("KM: {:.3f}".format(medida/1000))
print("HM: {:.2f}".format(medida/100))
print("DAM: {:.1f}".format(medida/10))
print("DM: {:.1f}".format(medida*10))
print("CM: {:.1f}".format(medida*100))
print("MM: {:.1f}".format(medida*1000))