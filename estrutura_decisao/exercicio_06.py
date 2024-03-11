#06-Faça um Programa que leia três números e mostre o maior deles.

def verifica_entrada(pergunta):
    while True:
        try:
            entrada = float(input(pergunta))
            return entrada
        except Exception:
            print("A entrada deve ser um número!")

def ordem_crescente(n1, n2, n3):
    maior = 0
    meio = 0
    menor = 0
    
    if(n1 > n2) and (n1 > n3):
        maior = n1
        if(n2 > n3):
            meio = n2
            menor = n3
        else:
            meio = n3
            menor = n2
    
    elif(n2 > n1) and (n2 > n3):
        maior = n2
        if(n1 > n3):
            meio = n1
            menor = n3
        else:
            meio = n3
            menor = n1
    
    elif(n3 > n1) and (n3 > n2):
        maior = n3
        if(n1 > n2):
            meio = n1
            menor = n2
        else:
            meio = n2
            menor = n1
    
    elif(n1 == n3) and (n2 < n1):
        maior = n1
        meio = n3
        menor = n2
    else:
        maior = n1
        meio = n2
        menor = n3
    return [maior, meio, menor]

def main():
    print("-" * 100)
    print(f"{'Esse programa mostra o maior número entre três.':^100}")
    print("-" * 100)

    n1 = verifica_entrada("Digite o 1º número: ")
    n2 = verifica_entrada("Digite o 2º número: ")
    n3 = verifica_entrada("Digite o 3º número: ")

    lista = ordem_crescente(n1, n2, n3)

    print("=" * 100)
    print(f"{f'Maior = {lista[0]}':^100}")
    print("=" * 100)

main()