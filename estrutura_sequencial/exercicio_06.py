#06-Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

print("Esse programa calcula a área de um círculo tendo como entrada o valor do raio.")
print("-" * 50)

raio = float(input("Digite o valor do raio do círculo(cm): "))

area = 3.14 * (raio ** 2)

print("-" * 50)
print(f"A área do círculo é de {area} cm²")