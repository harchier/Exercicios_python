#04-Faça um Programa que peça as 4 notas bimestrais e mostre a média.

print("Esse programa calcula a média de 4 notas bimestrais.")
print("-" * 50)

nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nota_3 = float(input("Digite a terceira nota: "))
nota_4 = float(input("Digite a quarta nota: "))

media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

print("-" * 50)
print(f"A média é: {media}")