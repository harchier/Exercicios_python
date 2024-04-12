# 51-Faça um programa que mostre os n termos da Série a seguir:
#   	S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
# 	Imprima no final a soma da série.

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_int(pergunta):
    while True:
        try:
            entrada = int(input(pergunta))
            if(entrada > 0):
                return entrada
            else:
                print("A entrada deve ser maior que 0.")
        except Exception:
            print("A entrada deve ser um número inteiro.")

def calcula_soma(n):
    soma = 0
    i = 1
    j = 1
    while(i <= n):
        soma += i/j
        i += 1
        j += 2
    return soma

def imprime_termos(n):
    if(n == 1):
        print("S = 1/1")
    else:
        print("S = ", end="")
        i = 1
        j = 1
        while(i < n):
            print(f"{i}/{j}", end=" + ")
            i += 1
            j += 2
        print(f"{i}/{j}.")

def main():
    cabecalho('Soma dos termos da série.')

    n = verifica_int("Digite o nº de itens: ")

    soma = calcula_soma(n)

    print("=" * 100)
    imprime_termos(n)
    print(f"Soma = {soma}")
    print("=" * 100)

main()