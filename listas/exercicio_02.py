#2-Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

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
                print("A entrada deve ser maior que 0.")
        except Exception:
            print("A entrada deve ser um número.")

def verifica_float(pergunta):
    while True:
        try:
            entrada = float(input(pergunta))
            return entrada
        except Exception:
            print("A entrada deve ser um número.")

def monta_lista(n):
    lista = []
    i = 1
    while(i <= n):
        numero = verifica_float(f"Digite o {i} número: ")
        lista.append(numero)
        i += 1
    return lista

def inverte_lista(lista):
    lista_invertida = []
    i = 1
    while(i <= len(lista)):
        lista_invertida.append(lista[-i])
        i += 1
    return lista_invertida

def imprime_lista(lista):
    i = 0
    while(i < (len(lista) - 1)):
        print(f"{lista[i]}", end=", ")
        i += 1
    print(f"{lista[i]}")

def main():
    cabecalho('Esse programa mostra uma lista invertida.')

    n = verifica_inteiro("Digite o número de elementos da lista: ")

    lista = monta_lista(n)

    lista_invertida = inverte_lista(lista)

    print("=" * 100)
    print("Lista = ", end="")
    imprime_lista(lista)
    print("Lista invertida = ", end="")
    imprime_lista(lista_invertida)
    print("=" * 100)

main()
    
