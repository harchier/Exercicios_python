# 50-Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_inteiro(pergunta):
    while True:
        try:
            entrada = int(input(pergunta))
            if(entrada > 0):
                return entrada
            else:
                print("A entrada deve ser um número positivo.")
        except Exception:
            print("A entrada deve ser um número inteiro.")

def soma_termos(n):
    i = 2
    h = 1
    while(i <= n):
        h += (1/i)
        i += 1
    return h

def imprime_termos(n):
    if(n == 1):
        print("H = 1")
    else:
        print("H = 1", end=" + ")
        i = 2
        while(i < n):
            print(f"1/{i}",end=" + ")
            i += 1
        print(f"1/{i}")

def main():
    cabecalho('Esse programa mostra a soma de progressão.')

    n = verifica_inteiro("Digite o nº de termos: ")

    h = soma_termos(n)

    print("=" * 100)
    imprime_termos(n)
    print(f"H = {h}")
    print("=" * 100)

main()