#13-Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

def cabecalho(texto):
    print("-" * 100)
    print(f"{f'{texto}':^100}")
    print("-" * 100)

def verifica_base(pergunta):
    while True:
        try:
            entrada = float(input(pergunta))
            return entrada
        except Exception:
            print("A base deve ser um número.")

def verifica_expoente(pergunta):
    while True:
        try:
            entrada = int(input(pergunta))
            return entrada
        except Exception:
            print("O expoente deve ser um número inteiro.")

def calcula_potencia(base, expoente):
    if(expoente < 0):
        base = 1 / base
        expoente = expoente * -1
        i = 1
        potencia = 1
        while(i <= expoente):
            potencia *= base
            i += 1
        return potencia
    elif(expoente == 0):
        potencia = 1
        return potencia
    else:
        i = 1
        potencia = 1
        while(i <= expoente):
            potencia *= base
            i += 1
        return potencia


def main():
    cabecalho('Esse programa calcula a potência de um número sem utilizar a função de potência.')
    print("x² --> base = x, expoente = 2")
    base = verifica_base("Digite o valor da base: ")
    expoente = verifica_expoente("Digite o valor do expoente: ")

    potencia = calcula_potencia(base, expoente)

    print("=" * 100)
    print(f"{potencia:.4f}")
    print("=" * 100)

main()

