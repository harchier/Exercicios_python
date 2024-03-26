#22-Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

def cabecalho(texto):
    print("-" * 100)
    print(f"{texto:^100}")
    print("-" * 100)

def verifica_entrada(pergunta):
    while True:
        try:
            entrada = int(input(pergunta))
            return entrada
        except Exception:
            print("A entrada deve ser um número inteiro.")

def verifica_primo(n):
    divisores = []
    n_divisores = 0
    i = 1
    while(i <= n):
        if(n % i == 0):
            n_divisores += 1
            divisores.append(i)
        i += 1
    if(n_divisores == 2):
        primo = True
    else:
        primo = False
    return [primo, divisores]

def main():
    cabecalho('Esse programa verifica se um número é primo e mostra os divisores.')

    n = verifica_entrada("Digite um número: ")

    primo_divisores = verifica_primo(n)

    print("=" * 100)
    if(primo_divisores[0] == True):
        print(f"{n} é primo.")
    else:
        print(f"{n} não é primo.")
    print(f"Divisores = {primo_divisores[1]}")
    print("=" * 100)

main()