#10-Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

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
        numero = verifica_float(f"Digite o {i}º número: ")
        lista.append(numero)
        i += 1
    return lista

def intercala_vetores(lista1, lista2):
    lista3 = []
    i = 0
    while(i < len(lista1)):
        lista3.append(lista1[i])
        lista3.append(lista2[i])
        i += 1
    return lista3

def main():
    cabecalho('Esse programa intercala dois vetores.')

    n = verifica_quantidade("Digite o tamanho dos vetores: ")

    print("Primeira Lista:")
    vetor_1 = monta_lista(n)
    print("-" * 100)
    print("Segunda Lista:")
    vetor_2 = monta_lista(n)

    vetor_3 = intercala_vetores(vetor_1, vetor_2)

    print("=" * 100)
    print(f"Vetor 1 = {vetor_1}")
    print(f"Vetor 2 = {vetor_2}")
    print(f"Vetor 3 = {vetor_3}")
    print("=" * 100)

main()
