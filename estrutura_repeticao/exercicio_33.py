# 33-O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_entrada(pergunta):
    while True:
        try:
            entrada = float(input(pergunta))
            return entrada
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
        temperatura = verifica_entrada(f"Digite a temperatura {i}: ")
        lista.append(temperatura)
        i += 1
    return lista

def percorre_lista(lista):
    maior = lista[0]
    menor = lista[0]
    soma = 0
    for e in lista:
        if(e > maior):
            maior = e
        if(e < menor):
            menor = e
        soma += e
    media = soma / len(lista)
    return [maior, menor, media]

def main():
    cabecalho('Esse programa mostra a maior, a menor e a media de um determinado número de temperaturas.')

    quantidade = verifica_quantidade("Digite o número de temperaturas: ")

    lista = monta_lista(quantidade)

    resultado = percorre_lista(lista)

    print("=" * 100)
    print(f"Maior = {resultado[0]} °C")
    print(f"Menor = {resultado[1]} °C")
    print(f"Média = {resultado[2]:.2f} °C")
    print("=" * 100)

main()