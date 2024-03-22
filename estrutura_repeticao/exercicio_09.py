#9-Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

def cabecalho(texto):
    print("-" * 100)
    print(f"{f'{texto}':^100}")
    print("-" * 100)

def verifica_entrada(pergunta):
    while True:
        try:
            entrada = int(input(pergunta))
            if(entrada > 0):    
                return entrada
        except Exception:
            print("A entrada deve ser um número.")

def imprime_impar(quantidade):
    i = 0
    e = 0
    while(e < quantidade):
        if(i % 2 != 0):
            print(i,end=" ")
            e += 1
        i += 1

def main():
    cabecalho('Esse programa imprime na tela a quantidade de números ímpares desejados.')

    quantidade = verifica_entrada("Digite a quantidade de números ímpares: ")
    print("=" * 200)
    imprime_impar(quantidade)
    print()
    print("=" * 200)

main()

