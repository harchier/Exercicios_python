# 39-Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_numero(pergunta):
    while True:
        try:
            numero = int(input(pergunta))
            if(numero > 0):
                return numero
            else:
                print("O número deve ser maior que 0.")
        except Exception:
            print("O número deve ser um número inteiro.")

def verifica_altura(pergunta):
    while True:
        try:
            altura = float(input(pergunta))
            if(altura > 0):
                return altura
            else:
                print("A altura deve ser maior que 0.")
        except Exception:
            print("A altura deve ser um número.")

def main():
    cabecalho('Esse programa encontra os alunos mais alto e mais baixo.')

    n_mais_alto = 0
    maior_altura = 0

    n_mais_baixo = 0
    menor_altura = float('inf')

    for i in range(10):
        numero = verifica_numero(f"Digite o número do aluno {i + 1}: ")
        altura = verifica_altura(f"Digite a altura do aluno {i + 1}(cm): ")

        if(altura > maior_altura):
            maior_altura = altura
            n_mais_alto = numero
        if(altura < menor_altura):
            menor_altura = altura
            n_mais_baixo = numero
    
    print("=" * 100)
    print(f"Mais alto: nº = {n_mais_alto} altura = {maior_altura} cm")
    print(f"Mais baixo: nº = {n_mais_baixo} altura = {menor_altura} cm")
    print("=" * 100)

main()