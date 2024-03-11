#08-Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

def verifica_entrada(pergunta):
    while True:
        try:
            entrada = float(input(pergunta))
            if(entrada > 0):
                return entrada
            else:
                print("O valor deve ser maior que 0.")
        except Exception:
            print("O valor deve ser um número.")

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
    print(f"{'Esse programa verifica o menor preço entre três produtos.'}")
    print("-" * 100)

    p1 = verifica_entrada("Digite o preço do produto a: ")
    p2 = verifica_entrada("Digite o preço do produto b: ")
    p3 = verifica_entrada("Digite o preço do produto c: ")
    
    dicionario = {"a":p1, "b":p2, "c":p3}

    lista = ordem_crescente(p1, p2, p3)
    
    print("=" * 100)
    for e in dicionario.keys():
        if(dicionario[e] == lista[2]):
            print(f"{f'Você deve comprar o produto {e}':^100}")
    print("=" * 100)
    

main()
