#16-A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.

def cabecalho(texto):
    print("-" * 100)
    print(f"{f'{texto}':^100}")
    print("-" * 100)

def verifica_maximo(pergunta):
    while True:
        try:
            maximo = int(input(pergunta))
            if(maximo > 0):
                return maximo
            else:
                print("O valor máximo deve ser maior que 0.")
        except Exception:
            print("O valor máximo deve ser um número inteiro.")

def gera_fibonacci(maximo):
    if(maximo == 1):
        lista = [1]
    elif(maximo == 2):
        lista = [1, 1, 2]
    else:
        lista = [1, 1]
        a = 1
        b = 1
        c = 2
        while(c <= maximo):
            c = a + b
            if(c > maximo):
                break
            lista.append(c)
            a = b
            b = c
    return lista

def main():
    cabecalho('Esse programa gera a sequência de Fibonacci até um determinado valor.')

    maximo = verifica_maximo("Digite o valor máximo a ser alcançado: ")

    lista = gera_fibonacci(maximo)

    print("=" * 100)
    print(f"Fibonacci até {maximo}: {lista}")
    print("=" * 100)

main()