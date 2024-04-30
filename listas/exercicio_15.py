#15-Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
	# a.Mostre a quantidade de valores que foram lidos;
	# b.Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
	# c.Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
	# d.Calcule e mostre a soma dos valores;
	# e.Calcule e mostre a média dos valores;
	# f.Calcule e mostre a quantidade de valores acima da média calculada;
	# g.Calcule e mostre a quantidade de valores abaixo de sete;
	# h.Encerre o programa com uma mensagem;

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_float(pergunta):
    while True:
        try:
            entrada = float(input(pergunta))
            if(entrada <= 10):
                return entrada
            else:
                print("A nota deve ser um número menor ou igual a 10. Tente novamente.")
        except Exception:
            print("A entrada deve ser um número. Tente novamente.")

def monta_lista():
    lista = []
    i = 1
    print("Digite um valor negativo para sair.(ex: -1)")
    while True:
        numero = verifica_float(f"Digite o {i}ª nota: ")
        if(numero < 0):
            break
        else:
            lista.append(numero)
            i += 1
    return lista

def imprime_lista(lista):
    print("Lista: ", end="")
    for e in lista:
        print(f"{e}", end=" ")
    print()

def imprime_lista_invertida(lista):
    print("Lista invertida: ")
    i = len(lista) - 1
    while(i >= 0):
        print(f"{i + 1}ª - {lista[i]}")
        i -= 1

def calcula_soma(lista):
    soma = 0
    for e in lista:
        soma += e
    return soma

def calcula_media(lista, soma):
    media = soma / len(lista)
    return media

def calcula_acima_media(lista, media):
    acima_media = 0
    for e in lista:
        if(e > media):
            acima_media += 1
    return acima_media

def calcula_abaixo_7(lista):
    abaixo_7 = 0
    for e in lista:
        if(e < 7):
            abaixo_7 += 1
    return abaixo_7

def main():
    cabecalho('Operações com listas.')

    lista = monta_lista()

    soma = calcula_soma(lista)
    media = calcula_media(lista, soma)

    acima_media = calcula_acima_media(lista, media)
    abaixo_7 = calcula_abaixo_7(lista)

    print("=" * 100)
    print(f"Quantidade de valores lidos: {len(lista)}")
    print("-" * 100)
    imprime_lista(lista)
    print("-" * 100)
    imprime_lista_invertida(lista)
    print("-" * 100)
    print(f"Soma = {soma:.2f}")
    print(f"Media = {media:.2f}")
    print(f"Quantidade de notas acima da média: {acima_media}")
    print(f"Quantidade de notas abaixo de 7: {abaixo_7}")
    print(f"Fique em paz!")
    print("=" * 100)

main()