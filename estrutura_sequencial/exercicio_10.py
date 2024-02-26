#10-Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
#C = 5 * ((F-32) / 9).
#c / 5 = (f - 32) / 9
#(c / 5) * 9 = f - 32
#F = ((c/5) * 9) + 32

print("Esse programa converte uma temperatura °C para °F.")
print("-" * 50)

c = float(input("Digite a temperatura em °C: "))
f = ((c/5) * 9) + 32

print("-" * 50)
print(f"{c} °C = {f:.2f} °F")
