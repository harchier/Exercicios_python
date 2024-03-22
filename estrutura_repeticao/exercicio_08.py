#8-Faça um programa que leia 5 números e informe a soma e a média dos números.

def cabecalho(texto):
    print("-" * 100)
    print(f"{f'{texto}':^100}")
    print("-" * 100)

def verifica_entrada(pergunta):
    while True:
        try:
            entrada = float(input(pergunta))
            return entrada
        except Exception:
            print("A entrada deve ser um número.")

def soma_elementos(lista):
    soma = 0
    for e in lista:
        soma += e
    return soma

def media_elementos(lista, soma):
    media = soma / len(lista)
    return media

def main():
    cabecalho('Esse programa informa a soma e a media entre 5 números.')

    lista = []
    i = 0
    while i < 5:
        numero = verifica_entrada(f"Digite o número {i + 1}: ")
        lista.append(numero)
        i += 1
    
    soma = soma_elementos(lista)
    media = media_elementos(lista, soma)

    print("=" * 100)
    print(f"{f'Números = {lista}':^100}")
    print(f"{f'Soma = {soma}':^100}")
    print(f"{f'Media = {media}':^100}")
    print("=" * 100)

main()