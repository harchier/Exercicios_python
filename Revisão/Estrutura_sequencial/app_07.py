#07-Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado = float(input("Digite o valor do lado em cm: "))

area = lado ** 2

print("-" * 100)
print(f"Área = {area} cm²")
print(f"Dobro da área = {area * 2} cm²")