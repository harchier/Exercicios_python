# 49-Faça um programa que mostre os n termos da Série a seguir:
#   	S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
# 	Imprima no final a soma da série.

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

def imprime_serie(n):
    print("S =",end=" ")
    soma = 0
    i = 1
    j = 1
    while(i < n):
        print(f"{i}/{j}",end=" + ")
        soma += (i / j)
        i += 1
        j += 2
    print(f"{i}/{j}.")
    print(f"Soma = {soma}")

def main():
    cabecalho('Esse programa imprime uma série de de números e mostra a soma deles.')

    n = verifica_inteiro("Digite o valor máximo da sequência: ")

    print("=" * 100)
    imprime_serie(n)
    print("=" * 100)

main()
