#23-Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_entrada(pergunta):
    while True:
        try:
            entrada = float(input(pergunta))
            return entrada   
        except Exception:
            print("A entrada deve ser um número.")

def e_inteiro(n):
    if(n % 1 == 0):
        inteiro = True
    else:
        inteiro = False
    return inteiro

def main():
    cabecalho('Esse programa informa se um número é inteiro ou decimal')

    n = verifica_entrada("Digite um número: ")
    inteiro = e_inteiro(n)

    print("=" * 100)
    if(inteiro == True):
        print(f"{f'{n} é inteiro.':^100}")
    else:
        print(f"{f'{n} é decimal.':^100}")
    print("=" * 100)

main()