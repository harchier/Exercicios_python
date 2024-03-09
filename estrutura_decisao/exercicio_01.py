#1-Faça um Programa que peça dois números e imprima o maior deles.

def verifica_entrada(pergunta):
    while True:
        try:
            entrada = float(input(pergunta))
            return entrada
        except Exception:
            print("O valor digitado deve ser um número.")

print("-" * 100)
print(f"{'Esse programa recebe dois números e indica qual é o maior.':^100}")
print("-" * 100)

n1 = verifica_entrada("Digite o 1º número: ")
n2 = verifica_entrada("Digite o 2º número: ")

print("=" * 100)
if(n1 > n2):
    maior = n1
    print(f"{f'O maior é {maior}.':^100}")
elif(n2 > n1):
    maior = n2
    print(f"{f'O maior é {maior}.':^100}")
else:
    print(f"{'Os valores são iguais.':^100}")
print("=" * 100)