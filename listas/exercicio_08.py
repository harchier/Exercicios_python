#8-Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_int(pergunta):
    while True:
        try:
            entrada = int(input(pergunta))
            if(entrada > 0):
                return entrada
            else:
                print("A entrada deve ser maior que 0.")
        except Exception:
            print("A entrada deve ser um número inteiro.")

def verifica_float(pergunta):
    while True:
        try:
            entrada = float(input(pergunta))
            if(entrada > 0):
                return entrada
            else:
                print("A entrada deve ser maior que 0.")
        except Exception:
            print("A entrada deve ser um número.")

def monta_lista(n):
    alturas = []
    idades = []
    i = 1
    while(i <= n):
        ida = verifica_int(f"Digite a idade da {i}ª pessoa: ")
        alt = verifica_float(f"Digite a altura da {i}ª pessoa: ")
        print("-" * 100)
        alturas.append(alt)
        idades.append(ida)
        i += 1
    return [idades, alturas]

def imprime_lista(idade, altura):
    i = len(idade) - 1
    while(i >= 0):
        print(f"Pessoa {i + 1}")
        print(f"{idade[i]} anos")
        print(f"{altura[i]} m")
        print("-" * 100)
        i -= 1
        
def main():
    cabecalho('Esse programa monta duas listas e imprime de trás para frente.')

    n = verifica_int("Digite o número de pessoas a registrar: ")

    listas = monta_lista(n)

    print("=" * 100)
    imprime_lista(listas[0], listas[1])
    print("=" * 100)

main()
