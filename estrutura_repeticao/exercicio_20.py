#20-Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

def cabecalho(texto):
    print("-" * 100)
    print(f"{texto:^100}")
    print("-" * 100)

def verifica_entrada(pergunta):
    while True:
        try:
            entrada = int(input(pergunta))
            if(0 <= entrada <= 16):
                return entrada
            else:
                print("A entrada deve ser um número entre 0 e 16.")
        except Exception:
            print("A entrada deve ser um número inteiro.")

def calcula_fatorial(n):
    f = 1
    while(n > 0):
        f *= n
        n -= 1
    return f

def main():
    cabecalho('Esse programa calcula o fatorial de um número menor que 16 múltiplas vezes.')
    
    while True:
        print("*" * 100)
        n = verifica_entrada("Digite o número a calcular o fatorial: ")

        fatorial = calcula_fatorial(n)

        print("=" * 100)
        print(f"Fatorial de {n} = {fatorial}")
        print("=" * 100)

        escolha = input("Deseja calcular outro fatorial?(s/n): ")
        escolha = escolha.lower()
        if(escolha == "n"):
            break

main()