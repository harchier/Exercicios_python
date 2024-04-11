# 48-Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
# 	Exemplo:
#   	12376489
#   	=> 98467321

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_entrada(pergunta):
    while True:
        entrada = input(pergunta)
        if(entrada.isnumeric() == True):
            return entrada
        else:
            print("A entrada deve ser numérica.")

def main():
    cabecalho('Esse programa mostra um número inteiro invertido.')

    n = verifica_entrada("Número: ")

    i = 1
    print("=>", end=" ")
    while(i <= len(n)):
        print(f"{n[-i]}",end="")    
        i += 1

main()