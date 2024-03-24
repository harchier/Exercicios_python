#17-Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

def cabecalho(texto):
    print("-" * 100)
    print(f"{texto:^100}")
    print("-" * 100)

def verifica_entrada(pergunta):
    while True:
        try:
            entrada = int(input(pergunta))
            if(entrada >= 0):
                return entrada
            else:
                print("A entrada não pode ser menor que 0.")
        except Exception:
            print("A entrada deve ser um número inteiro.")

def calcula_fatorial(n):
    f = 1
    while(n > 0):
        f *= n
        n -= 1
    return f

def main():
    cabecalho('Esse programa calcula o fatorial de um número.')

    n = verifica_entrada("Digite o número a calcular o fatorial: ")

    fatorial = calcula_fatorial(n)

    print("=" * 100)
    print(f"Fatorial de {n} = {fatorial}")
    print("=" * 100)

main()