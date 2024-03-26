#24-Faça um programa que calcule o mostre a média aritmética de N notas.

def cabecalho(texto):
    print("-" * 100)
    print(f"{texto:^100}")
    print("-" * 100)

def verifica_entrada(pergunta):
    while True:
        try:
            entrada = float(input(pergunta))
            if(0 <= entrada <= 10):
                return entrada
            else:
                print("A entrada deve ser um número entre 0 e 10.")
        except Exception:
            print("A entrada deve ser um número inteiro.")

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

def calcula_media(lista):
    soma = 0
    for e in lista:
        soma += e
    media = soma / len(lista)
    return media

def gera_lista(n):
    lista = []
    i = 1
    while(i <= n):
        nota = verifica_entrada(f"Digite a nota {i}: ")
        lista.append(nota)
        i += 1
    return lista

def main():
    cabecalho('Esse programa calcula a média de N notas.')
    n = verifica_quantidade("Digite a quantidade de notas: ")
    lista = gera_lista(n)
    media = calcula_media(lista)

    print("=" * 100)
    print(f"Notas = {lista}")
    print(f"Media = {media:.2f}")
    print("=" * 100)

main()