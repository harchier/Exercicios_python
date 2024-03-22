#7-Faça um programa que leia 5 números e informe o maior número.

def cabecalho(texto):
    print("-" * 100)
    print(f"{f'{texto}':^100}")
    print("-" * 100)

def verifica_entrada(pergunta):
    while True:
        try:
            entrada = float(input(pergunta))
            return entrada
        except Exception:
            print("A entrada deve ser um número.")

def main():
    cabecalho('Esse programa informa o maior número entre 5.')

    maior = float('-inf')
    i = 0
    while i < 5:
        numero = verifica_entrada(f"Digite o número {i + 1}: ")
        if(numero > maior):
            maior = numero
        i += 1
    
    print("=" * 100)
    print(f"{f'O maior número digitado foi {maior}':^100}")
    print("=" * 100)

main()