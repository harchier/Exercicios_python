#23-Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

def cabecalho(texto):
    print("-" * 100)
    print(f"{texto:^100}")
    print("-" * 100)

def verifica_entrada(pergunta):
    while True:
        try:
            entrada = int(input(pergunta))
            if(entrada > 1):
                return entrada
            else:
                print("A entrada deve ser maior que 1.")
        except Exception:
            print("A entrada deve ser um número inteiro.")

def verifica_primo(n):
    divisores = 0
    i = 1
    while(i <= n):
        if(n % i == 0):
            divisores += 1
        i += 1
    if(divisores == 2):
        primo = True
    else:
        primo = False
    return primo

def gera_primos(n):
    lista = []
    i = 0
    while(i <= n):
        e_primo = verifica_primo(i)
        if(e_primo == True):
            lista.append(i)
        i += 1
    return lista

def main():
    cabecalho('Esse programa mostra uma quantidade de números primos.')
    print("O programa gerará uma lista de números primos de 1 até n.")
    n = verifica_entrada("Digite n: ")

    lista = gera_primos(n)

    print("=" * 100)
    print(f"Lista de primos até {n} = {lista}")
    print("=" * 100)

main()