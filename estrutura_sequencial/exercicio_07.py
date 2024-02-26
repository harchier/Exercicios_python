#07-Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

print("Esse programa calcula a área de um quadrado e mostra o dobro dessa área para o usuário.")
print("-" * 50)

lado = float(input("Digite o valor do lado(cm): "))

area = lado ** 2

print(f"O dobro da área é {area * 2} cm²")