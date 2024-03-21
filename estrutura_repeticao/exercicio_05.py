#5-Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

def cabecalho(texto):
    print("-" * 100)
    print(f"{f'{texto}':^100}")
    print("-" * 100)

def verifica_populacao(pergunta):
    while True:
        try:
            populacao = int(input(pergunta))
            if(populacao > 0):
                return populacao
            else:
                print("A população deve ser um maior que 0.")
        except Exception:
            print("A população deve ser um número.")

def verifica_taxa(pergunta):
    while True:
        try:
            taxa = float(input(pergunta))
            return taxa
        except Exception:
            print("A taxa deve ser um número.")

def main():
    cabecalho('Esse programa calcula quando duas populações irão se igualar.')
    
    #achar as fórmulas para as duas populações.
    pa = verifica_populacao("Digite a população A: ")
    pb = verifica_populacao("Digite a população B: ")

    if(pa == pb):
        print("=" * 100)
        print(f"{f'As populações já são iguais.':^100}")
        print("=" * 100)
    else:
        txa = verifica_taxa("Digite a taxa de crescimento de A (%): ")
        txb = verifica_taxa("Digite a taxa de crescimento de B (%): ")
        
        txa_d = txa / 100
        txb_d = txb / 100

        b1 = pa
        a1 = pa * txa_d

        b2 = pb
        a2 = pb * txb_d

        #formula para as duas equações se encontratem no x
        if(a1 - a2 == 0):
            x = -1
        else:
            x = (pb - pa) / (a1 - a2)

        print("=" * 100)
        if(x < 0):
            print(f"{f'As populações nunca irão se igualar.':^100}")
        else: 
            print(f"{f'As populações irão se igualar em {x} anos.':^100}")
        print("=" * 100)

main()

