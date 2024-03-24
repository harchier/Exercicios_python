#19-Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

def cabecalho(texto):
    print("-" * 100)
    print(f"{texto:^100}")
    print("-" * 100)

def verifica_entrada(pergunta):
    while True:
        try:
            entrada = float(input(pergunta))
            if(0 <= entrada <= 1000):
                return entrada
            else:
                print("A entrada deve ser um número entre 0 e 1000.")
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
            print("A quantidade deve ser um número inteiro.")

def monta_lista(quantidade):
    lista = []
    i = 1
    while(i <= quantidade):
        n = verifica_entrada(f"Digite o número {i}: ")
        lista.append(n)
        i += 1
    return lista

def define_maior(lista):
    maior = lista[0]
    for e in lista:
        if(e > maior):
            maior = e
    return maior

def define_menor(lista):
    menor = lista[0]
    for e in lista:
        if(e < menor):
            menor = e
    return menor

def soma_elementos(lista):
    soma = 0
    for e in lista:
        soma += e
    return soma

def main():
    cabecalho('Esse programa determina o maior, o menor e a soma de um conjunto de números.')

    quantidade = verifica_quantidade("Digite a quantidade de números: ")

    lista = monta_lista(quantidade)

    maior = define_maior(lista)
    menor = define_menor(lista)
    soma = soma_elementos(lista)

    print("=" * 100)
    print(f"Maior = {maior}")
    print(f"Menor = {menor}")
    print(f"Soma = {soma}")
    print("=" * 100)

main()
