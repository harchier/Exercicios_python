#10-Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

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
            print("A entrada deve ser um número inteiro.")

def gera_inteiros(min,max):
    if(max <= min):
        print("O valor máximo deve ser maior que o mínimo.",end="")
    else:
        i = min
        while(i <= max):
            print(i,end=" ")
            i += 1

def main():
    cabecalho('Esse programa mostra os números inteiros existentes em um intervalo.')

    min = verifica_entrada("Digite o valor inicial: ")
    max = verifica_entrada("Digite o valor final: ")
    print("=" * 100)
    gera_inteiros(min, max)
    print()
    print("=" * 100)

main()