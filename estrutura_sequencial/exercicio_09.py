#09-Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
    #C = 5 * ((F-32) / 9).

print("Esse programa converte uma temperatura °F para °C.")
print("-" * 50)

f = float(input("Digite a temperatura em °F: "))
c = 5 * ((f - 32) / 9)

print("-" * 50)
print(f"{f} °F = {c:.2f} °C")