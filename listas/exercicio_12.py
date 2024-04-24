#12-Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_quantidade(pergunta):
    while True:
        try:
            entrada = int(input(pergunta))
            if(entrada > 0):
                return entrada
            else:
                print("A entrada deve ser maior que 0.")
        except Exception:
            print("A entrada deve ser um número inteiro.")

def verifica_float(pergunta):
    while True:
        try:
            entrada = float(input(pergunta))
            if(entrada > 0):
                return entrada
            else:
                print("A entrada deve ser positiva.")
        except Exception:
            print("A entrada deve ser um número.")

def monta_lista(n):
    lista = []
    i = 1
    while(i <= n):
        numero = verifica_float(f"Digite a {i}ª altura: ")
        lista.append(numero)
        i += 1
    return lista

def calcula_media(lista):
    soma = 0
    for e in lista:
        soma += e
    media = soma / len(lista)
    return media

def abaixo_media(lista, media):
    n_abaixo_media = 0
    for e in lista:
        if(e < media):
            n_abaixo_media += 1
    return n_abaixo_media

def main():
    cabecalho('Esse programa verifica a quantidade de alunos com altura abaixo da média.')

    n = verifica_quantidade("Digite a quantidade de alunos: ")

    lista = monta_lista(n)

    media = calcula_media(lista)

    n_abaixo_media = abaixo_media(lista, media)

    print("=" * 100)
    print(f"Media = {media} m")
    print(f"Número de alunos com altura abaixo da média = {n_abaixo_media}")
    print("=" * 100)

main()