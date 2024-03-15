#17-Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_entrada(pergunta):
    while True:
        try:
            entrada = int(input(pergunta))
            if(entrada > 0):
                return entrada
            else:
                print("A entrada deve ser maior que zero.")
        except Exception:
            print("A entrada deve ser um número.")

def verifica_bissexto(ano):
    if(ano % 4 == 0):
        if(ano % 100 == 0):
            if(ano % 400 == 0):
                bissexto = True
            else:
                bissexto = False
        else:
            bissexto = True
    else:
        bissexto = False
    return bissexto

def main():
    cabecalho('Esse programa verifica se um ano é bissexto.')
    
    ano = verifica_entrada("Digite o ano: ")
    bissexto = verifica_bissexto(ano)
    
    print("=" * 100)
    if(bissexto == True):
        print(f"{f'{ano} é bissexto.':^100}")
    else:
        print(f"{f'{ano} não é bissexto.':^100}")
    print("=" * 100)

main()