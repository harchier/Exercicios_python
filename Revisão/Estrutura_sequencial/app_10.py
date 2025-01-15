#10-Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

temperatura_c = float(input("Digite a temperatura em ºC: "))

temperatura_f = ((temperatura_c / 5) * 9) + 32

print("-" * 100)
print(f"{temperatura_c}ºC = {temperatura_f}ºF")