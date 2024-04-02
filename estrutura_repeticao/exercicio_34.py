# 34-Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_entrada(pergunta):
    while True:
        try:
            entrada = int(input(pergunta))
            return entrada
        except Exception:
            print("A entrada deve ser um número.")

def verifica_primo(n):
    i = 1
    d = 0
    while(i <= n):
        if(n % i == 0):
            d += 1
        i += 1
    if(d == 2):
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