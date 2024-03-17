#22-Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_entrada(pergunta):
    while True:
        try:
            entrada = int(input(pergunta))
            return entrada   
        except Exception:
            print("A entrada deve ser um número.")

def e_par(n):
    if(n % 2 == 0):
        par = True
    else:
        par = False
    return par

def main():
    cabecalho('Esse programa mostra se um número é par ou ímpar.')

    n = verifica_entrada("Digite um número inteiro: ")
    paridade = e_par(n)
    
    print("=" * 100)
    if(paridade == True):
        print(f"{f'{n} é par.':^100}")
    else:
        print(f"{f'{n} é ímpar.':^100}")
    print("=" * 100)

main()