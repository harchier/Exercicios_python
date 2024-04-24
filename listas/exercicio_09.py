#9-Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_quantidade(pergunta):
    while True:
        try:
            entrada = int(input(pergunta))
            if(entrada > 0):
                return entrada
            else:
                print("A entrada deve ser maior que 0.")
        except Exception:
            print("A entrada deve ser um número inteiro.")

def verifica_int(pergunta):
    while True:
        try:
            entrada = int(input(pergunta))
            return entrada
        except Exception:
            print("A entrada deve ser um número inteiro.")

def monta_lista(n):
    lista = []
    i = 1
    while(i <= n):
        numero = verifica_int(f"Digite o {i}º número: ")
        lista.append(numero)
        i += 1
    return lista

def soma_lista(lista):
    soma = 0
    for e in lista:
        x = e ** 2
        soma += x
    return soma

def main():
    cabecalho('Esse program mostra a soma dos quadrados dos elementos de uma lista.')

    n = verifica_quantidade("Digite a quantidade de elementos da lista: ")

    lista = monta_lista(n)

    soma = soma_lista(lista)

    print("=" * 100)
    print(f"Lista = {lista}")
    print(f"Soma dos quadrados = {soma}")
    print("=" * 100)

main()