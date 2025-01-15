#06-Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math

raio = float(input("Digite o valor do raio em metros: "))

area = 2 * math.pi * (raio ** 2)

print("-" * 100)
print(f"Área do círculo = {area} m²")