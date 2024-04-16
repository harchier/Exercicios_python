#1-Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_inteiro(pergunta):
    while True:
        try:
            entrada = int(input(pergunta))
            return entrada
        except Exception:
            print("A entrada deve ser um número.")

def monta_lista(n):
    lista = []
    for i in range(n):
        numero = verifica_inteiro(f"Digite o {i + 1} número: ")
        lista.append(numero)
    return lista

def imprime_lista(lista):
    i = 0
    while(i < (len(lista) - 1)):
        print(f"{lista[i]}", end=", ")
        i += 1
    print(lista[i])

def main():
    cabecalho('Esse program monta uma lista.')

    n = 5
    
    lista = monta_lista(n)

    print("=" * 100)
    print("Lista = ", end=" ")
    imprime_lista(lista)
    print("=" * 100)

main()
