#6-Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.

def cabecalho(texto):
    print("-" * 100)
    print(f"{f'{texto}':^100}")
    print("-" * 100)

def verifica_entrada(pergunta):
    while True:
        try:
            entrada = int(input(pergunta))
            if(1 <= entrada <= 2):
                return entrada
            else:
                print("A entrada deve ser um 1 ou 2.")
        except Exception:
            print("A entrada deve ser um número.")

def verifica_quantidade(pergunta):
    while True:
        try:
            quantidade = int(input(pergunta))
            if(quantidade > 0):
                return quantidade
            else:
                print("A quantidade deve ser maior que 0.")
        except Exception:
            print("A quantidade deve ser um número.")

def numeros_abaixo(quantidade):
    i = 1
    while(i <= quantidade):
        print(i)
        i += 1

def numeros_ao_lado(quantidade):
    i = 1
    while(i <= quantidade):
        print(i,end=" ")
        i += 1
    print()

def main():
    cabecalho('Esse programa mostra uma quantidades de números inteiros empilhados ou lado a lado.')
    
    quantidade = verifica_quantidade("Digite a quantidade de números a imprimir: ")
    escolha = verifica_entrada("Você quer os números empilhados(1) ou lado a lado(2)? ")

    if(escolha == 1):
        print("=" * 3)
        numeros_abaixo(quantidade)
        print("=" * 3)
    else:
        print("=" * (quantidade * 3))
        numeros_ao_lado(quantidade)
        print("=" * (quantidade * 3))

main()