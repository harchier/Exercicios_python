#3-Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_inteiro(pergunta):
    while True:
        try:
            entrada = int(input(pergunta))
            if(entrada > 0):
                return entrada
            else:
                print("A entrada deve ser maior que 0")
        except Exception:
            print("A entrada deve ser um número.")

def verifica_float(pergunta):
    while True:
        try:
            entrada = float(input(pergunta))
            if(0 <= entrada <= 10):
                return entrada
            else:
                print("A entrada deve ser um valor entre 0 e 10.")
        except Exception:
            print("A entrada deve ser um número.")

def monta_lista(n):
    lista = []
    i = 1
    while(i <= n):
        nota = verifica_float(f"Digite a {i}ª nota: ")
        lista.append(nota)
        i += 1
    return lista

def mostra_notas(lista):
    i = 0
    while(i <= len(lista) - 1):
        print(f"{i + 1}ª nota: {lista[i]}")
        i += 1

def main():
    cabecalho('Esse programa calcula a media de um determinado número de notas.')

    n = verifica_inteiro("Digite o nº de notas: ")

    lista = monta_lista(n)
    
    soma = 0
    for e in lista:
        soma += e
    
    media = soma / n

    print("=" * 100)
    mostra_notas(lista)
    print("-" * 100)
    print(f"Media = {media}")
    print("=" * 100)

main()

