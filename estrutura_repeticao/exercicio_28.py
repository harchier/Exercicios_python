# 28-Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

def cabecalho(texto):
    print("-" * 100)
    print(f"{texto:^100}")
    print("-" * 100)

def verifica_quantidade(pergunta):
    while True:
        try:
            quantidade = int(input(pergunta))
            if(quantidade > 0):
                return quantidade
            else:
                print("A quantidade deve ser um número maior que 0.")
        except Exception:
            print("A quantidade deve ser um número inteiro.")

def verifica_valor(pergunta):
    while True:
        try:
            valor = float(input(pergunta))
            if(valor > 0):
                return valor
            else:
                print("O valor deve ser maior que 0.")
        except Exception:
            print("O valor deve ser um número.")

def calcula_media(quantidade):
    soma = 0
    for e in range(quantidade):
        valor = verifica_valor(f"Digite o valor do produto {e + 1}: ")
        soma += valor
    media = soma / quantidade
    return media

def main():
    cabecalho('Esse programa calcula o preço medio de produtos.')

    quantidade = verifica_quantidade("Digite a quantidade de objetos: ")

    media = calcula_media(quantidade)

    print("=" * 100)
    print(f"Preço medio por produto = R$ {media:.2f}")
    print("=" * 100)

main()