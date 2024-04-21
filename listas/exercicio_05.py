#5-Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

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

def verifica_tamanho(pergunta):
    while True:
        try:
            entrada = int(input(pergunta))
            if(entrada > 0):
                return entrada
            else:
                print("A entrada deve ser maior que 0.")
        except Exception:
            print("A entrada deve ser um número inteiro.")

def verifica_par(n):
    par = False
    if(n % 2 == 0):
        par = True
    return par

def monta_lista(n):
    lista = []
    i = 0
    while(i < n):
        numero = verifica_inteiro(f"Digite o {i + 1}º número: ")
        lista.append(numero)
        i += 1
    return lista

def main():
    cabecalho('Esse programa monta e separa uma lista.')

    n = verifica_tamanho("Digite o tamanho da lista: ")

    lista = monta_lista(n)

    pares = []
    impares = []
    for e in lista:
        par = verifica_par(e)
        if(par == True):
            pares.append(e)
        else:
            impares.append(e)
    
    print("=" * 100)
    print(f"Lista = {lista}")
    print(f"Pares = {pares}")
    print(f"Ímpares = {impares}")
    print("=" * 100)

main()