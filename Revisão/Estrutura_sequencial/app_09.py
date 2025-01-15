#09-Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#    C = 5 * ((F-32) / 9).

temperatura_f = float(input("Digite o valor da temperatura em ºF: "))

temperatura_c = 5 * ((temperatura_f - 32) / 9)

print("-" * 100)
print(f"{temperatura_f}ºF = {temperatura_c}ºC")