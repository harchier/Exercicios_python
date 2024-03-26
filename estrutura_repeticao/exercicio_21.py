#21-Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

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
    divisores = 0
    i = 1
    while(i <= n):
        if(n % i == 0):
            divisores += 1
        i += 1
    if(divisores == 2):
        primo = True
    else:
        primo = False
    return primo

def main():
    cabecalho('Esse programa verifica se um número é primo.')

    n = verifica_entrada("Digite um número: ")

    primo = verifica_primo(n)

    print("=" * 100)
    if(primo == True):
        print(f"{n} é primo.")
    else:
        print(f"{n} não é primo.")
    print("=" * 100)

main()