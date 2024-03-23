#14-Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

def cabecalho(texto):
    print("-" * 100)
    print(f"{f'{texto}':^100}")
    print("-" * 100)

def verifica_entrada(pergunta):
    while True:
        try:
            entrada = int(input(pergunta))
            return entrada
        except Exception:
            print("A entrada deve ser um número.")

def verifica_quantidade(pergunta):
    while True:
        try:
            quantidade = int(input(pergunta))
            if(quantidade > 0):
                return quantidade
            else:
                print("A quantidade deve ser maior que 0.")
        except Exception:
            print("A quantidade deve ser um número inteiro.")

def monta_lista(quantidade):
    lista = []
    i = 1
    while(i <= quantidade):
        n = verifica_entrada(f"Digite o {i} número: ")
        lista.append(n)
        i += 1
    return lista

def separa_pares(lista):
    pares = []
    for e in lista:
        if(e % 2 == 0):
            pares.append(e)
    return pares

def separa_impares(lista):
    impares = []
    for e in lista:
        if(e % 2 != 0):
            impares.append(e)
    return impares

def main():
    cabecalho('Esse programa lista os pares e impares em uma sequência.')

    quantidade = verifica_quantidade("Digite a quantidade de números na sequência: ")
    lista = monta_lista(quantidade)
    pares = separa_pares(lista)
    impares = separa_impares(lista)

    print("=" * 100)
    print(f"Números: {lista}")
    print(f"Pares: {pares}, quantidade: {len(pares)}")
    print(f"Ímpares: {impares}, quantidade: {len(impares)}")
    print("=" * 100)

main()