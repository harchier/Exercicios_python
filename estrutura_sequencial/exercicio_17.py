#17-Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#     comprar apenas latas de 18 litros;
#     comprar apenas galões de 3,6 litros;
#     misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

def verifica_entrada(pergunta):
    while True:
        try:
            entrada = float(input(pergunta))
            if(entrada > 0):
                return entrada
            else:
                print("O valor da entrada deve ser maior que 0.")
        except Exception:
            print("O valor da entrada deve ser um número.")

print("-" * 100)
print(f"{'Esse programa calcula o número de latas e galões para uma área a ser pintada.':^100}")
print("-" * 100)

area = verifica_entrada("Digite o tamanho da área a ser pintada(m²): ")
litros = area / 6
litros = litros + (litros * 0.1)

#comprando apenas latas
latas = litros // 18
sobra_latas = litros % 18
if(sobra_latas != 0):
    latas += 1
sobra_tinta = 18 - sobra_latas
preco = latas * 80
print(f"A quantidade de litros é de {litros:.2f} L")
print("=" * 100)
print("Comprando apenas latas:")
print(f"Número de latas: {latas}")
print(f"Preço: R$ {preco}")
print(f"Sobra de tinta: {sobra_tinta:.2f} L")

#comprando apenas galões
galoes = litros // 3.6
sobra_galoes = litros % 3.6
if(sobra_galoes != 0):
    galoes += 1
sobra_tinta = 3.6 - sobra_galoes
preco = galoes * 25
print("=" * 100)
print("Comprando apenas Galões:")
print(f"Número de galões: {galoes}")
print(f"Preço: R$ {preco}")
print(f"Sobra de tinta: {sobra_tinta:.2f} L")

#comprando latas e galoes
latas = litros // 18
sobra_latas = litros % 18
galoes = sobra_latas // 3.6
sobra_galoes = sobra_latas % 3.6
if(sobra_galoes != 0):
    galoes += 1
sobra_tinta = 3.6 - sobra_galoes
preco = (latas * 80) + (galoes * 25)
print("=" * 100)
print("Comprando Latas e Galões:")
print(f"O número de latas é {latas}")
print(f"O número de galões é {galoes}")
print(f"O preço a pagar será de R$ {preco}")
print(f"A sobra de tinta será de {sobra_tinta:.2f} L")

