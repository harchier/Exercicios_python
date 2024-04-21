#7-Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

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
            print("A entrada deve ser um número inteiro.")

def verifica_tamnho(pergunta):
    while True:
        try:
            entrada = int(input(pergunta))
            if(entrada > 0):
                return entrada
            else:
                print("A entrada deve ser maior que 0.")
        except Exception:
            print("A entrada deve ser um número.")

def monta_lista(n):
    lista = []
    i = 1
    while(i <= n):
        numero = verifica_inteiro(f"Digite o {i}º numero:")
        lista.append(numero)
        i += 1
    return lista

def soma_lista(lista):
    soma = 0
    for e in lista:
        soma += e
    return soma

def multiplica_lista(lista):
    m = 1
    for e in lista:
        m *= e
    return m

def imprime_lista(lista):
    for e in lista:
        print(f"{e}", end=" ")
    print()

def main():
    cabecalho('Esse programa monta uma lista, soma e multiplica seus elementos.')

    n = verifica_tamnho("Digite o tamanho da lista: ")

    lista = monta_lista(n)

    soma = soma_lista(lista)
    multiplicacao = multiplica_lista(lista)

    print("=" * 100)
    print("Lista: ", end="")
    imprime_lista(lista)
    print(f"Soma = {soma}")
    print(f"Multiplicação = {multiplicacao}")
    print("=" * 100)

main()
