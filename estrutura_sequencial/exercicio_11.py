#11-Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    # o produto do dobro do primeiro com metade do segundo .
    # a soma do triplo do primeiro com o terceiro.
    # o terceiro elevado ao cubo.

print("Esse programa realiza operações simples com números inteiros.")
print("-" * 50)

x = int(input("Digite um número inteiro: "))
y = int(input("Digite outro número inteiro: "))
z = float(input("Digite um número real: "))

a = (x * 2) * (y / 2)
b = (x * 3) + z
c = z ** 3

print("-" * 50)
print(f"O produto do dobro do primeiro com metade do segundo = {a}")
print(f"A soma do triplo do primeiro com o terceiro = {b}")
print(f"O terceiro elevado ao cubo = {c}")