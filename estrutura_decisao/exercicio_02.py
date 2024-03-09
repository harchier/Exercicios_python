#2-Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

def verifica_entrada(pergunta):
    while True:
        try:
            entrada = float(input(pergunta))
            return entrada
        except Exception:
            print("O valor deve ser um número.")

print("-" * 100)
print(f"{'Esse programa verifica se um número é positivo ou negaivo':^100}")
print("-" * 100)

n = verifica_entrada("Digite um número: ")

print("=" * 100)
if(n > 0):
    print(f"{f'O número {n} é positivo.':^100}")
elif(n < 0):
    print(f"{f'O número {n} é negativo.':^100}")
else:
    print(f"{f'O número {n} é nulo':^100}")
print("=" * 100)