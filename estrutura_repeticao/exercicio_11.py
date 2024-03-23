#11-Altere o programa anterior para mostrar no final a soma dos números.

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
        lista = []
        i = min
        while(i <= max):
            lista.append(i)
            i += 1
        return lista

def soma_elementos(lista):
    soma = 0
    for e in lista:
        soma += e
    return soma

def main():
    cabecalho('Esse programa mostra os números inteiros existentes em um intervalo e a soma deles.')

    min = verifica_entrada("Digite o valor inicial: ")
    max = verifica_entrada("Digite o valor final: ")
    
    lista = gera_inteiros(min, max)
    soma = soma_elementos(lista)
    print("=" * 100)
    for e in lista:
        print(e,end=", ")
    print()
    print(f"{f'Soma = {soma}':<100}")
    print("=" * 100)

main()