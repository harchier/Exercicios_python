#16-Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

def verifica_entrada(pergunta):
    while True:
        try:
            entrada = float(input(pergunta))
            if(entrada > 0):
                return entrada
            else:
                print("O valor da entrada deve ser positivo.")
        except Exception:
            print("O valor da entrada deve ser um número!")
    

print("-" * 100)
print("Esse programa calcula o número de latas de tintas a serem compradas.")
print("-" * 100)

area = verifica_entrada("Digite o valor da área(m²): ")
litros = area / 3
if(litros % 1 == 0):
    latas = litros / 18
else:
    latas = (litros // 18) + 1
sobra = (latas * 18) - litros

print("=" * 100)
print(f"A quantidade de tinta necessária é de {litros:.2f} L")
print(f"O número de latas necessárias é de {latas}")
print(f"Sobrará {sobra:.2f} L de tinta.")
print("=" * 100)