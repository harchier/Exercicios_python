#4-Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_int(pergunta):
    while True:
        try:
            entrada = int(input(pergunta))
            if(entrada > 0):
                return entrada
            else:
                print("A entrada deve ser maior que 0")
        except Exception:
            print("A entrada deve ser um número.")

def monta_lista(n):
    consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n' , 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    lista = []
    i = 0
    while(i <= n):
        entrada = input("Digite alguma coisa: ")
        entrada = entrada.lower()
        if(entrada in consoantes):
            lista.append(entrada)
        i += 1
    return lista

def main():
    cabecalho('Esse programa mostra quantas consoantes foram digitadas.')

    n = verifica_int("Digite o número de termos a serem verificados: ")

    lista = monta_lista(n)

    print("=" * 100)
    print("Consoantes digitadas: ", end="")
    for e in lista:
        print(f"{e}", end=" ")
    print(f"\nNúmero de consoantes digitadas: {len(lista)}")
    print("=" * 100)

main()