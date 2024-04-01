# 32-Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
# 	Fatorial de: 5
# 	5! =  5 . 4 . 3 . 2 . 1 = 120

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_entrada(pergunta):
    while True:
        try:
            entrada = int(input(pergunta))
            if(entrada >= 0):
                return entrada
            else:
                print("A entrada deve ser maior ou igual a 0.")
        except Exception:
            print("A entrada deve ser um número.")

def calcula_fatorial(n):
    f = 1
    while(n > 1):
        f *= n
        n -= 1
    return f

def imprime_fatorial(n, fat):
    if(n > 1):
        print(f"{n}! =",end=" ")
        while(n > 1):
            print(f"{n}",end=" . ")
            n -= 1
        print(f"1 = {fat}")
    else:
        print(f"{n}! = 1")

def main():
    cabecalho('Esse programa calcula o fatorial de um número.')

    n = verifica_entrada("Digite um número: ")

    fat = calcula_fatorial(n)

    print("=" * 100)
    imprime_fatorial(n, fat)
    print("=" * 100)

main()

