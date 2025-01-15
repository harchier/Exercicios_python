#11-Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#    o produto do dobro do primeiro com metade do segundo .
#    a soma do triplo do primeiro com o terceiro.
#    o terceiro elevado ao cubo.

numero_1 = int(input("Digite o primeiro número (inteiro): "))
numero_2 = int(input("Digite o segundo número (inteiro): "))
numero_3 = float(input("Digite o terceiro número (real)"))

operacao_1 = (numero_1 * 2) * (numero_2 / 2)
operacao_2 = (numero_1 * 3) + numero_3
operacao_3 = numero_3 ** 3

print("-" * 100)
print(f"O produto do dobro do primeiro com metade do segundo = {operacao_1}")
print(f"A soma do triplo do primeiro com o terceiro = {operacao_2}")
print(f"o terceiro elevado ao cubo. = {operacao_3}")