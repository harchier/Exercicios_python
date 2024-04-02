#35-Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
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
            print("A entrada deve ser um número.")

def verifica_primo(n):
    i = 1
    d = 0
    while(i <= n):
        if(n % i == 0):
            d += 1
        i += 1
    if(d == 2):
        primo = True
    else:
        primo = False
    return primo

def monta_lista(numero):
    lista =[]
    i = 1
    while(i <= numero):
        e_primo = verifica_primo(i)
        if(e_primo == True):
            lista.append(i)
        i += 1
    return lista

def main():
    cabecalho('Esse programa mostra uma sequência de números primos.')

    n = verifica_entrada("Digite o número máximo da lista de primos: ")

    lista = monta_lista(n)

    print("=" * 100)
    for e in lista:
        print(f"{e}",end=" ")
    print()
    print("=" * 100)

main()