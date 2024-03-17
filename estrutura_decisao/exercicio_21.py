#21-Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
	# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
	# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_entrada(pergunta):
    while True:
        try:
            entrada = float(input(pergunta))
            if(10 <= entrada <= 600):
                return entrada
            else:
                print("A entrada deve ser maior que 10 e menor que 600.")
        except Exception:
            print("A entrada deve ser um número.")

def numero_notas(valor):
    lista = []
    n_100 = valor // 100
    sobra_100 = valor % 100
    n_50 = sobra_100 // 50
    sobra_50 = sobra_100 % 50
    n_10 = sobra_50 // 10
    sobra_10 = sobra_50 % 10
    n_5 = sobra_10 // 5
    sobra_5 = sobra_10 % 5
    n_1 = sobra_5 // 1

    lista.append(n_100)
    lista.append(n_50)
    lista.append(n_10)
    lista.append(n_5)
    lista.append(n_1)
    return lista


def main():
    cabecalho('Esse programa simula um caixa eletrônico')

    valor = verifica_entrada("Digite o valor(10-600): ")
    lista_notas = numero_notas(valor)
    
    print("=" * 28)
    print(f"{f'Notas de 100: {lista_notas[0]}':<100}")
    print(f"{f'Notas de 50:  {lista_notas[1]}':<100}")
    print(f"{f'Notas de 10:  {lista_notas[2]}':<100}")
    print(f"{f'Notas de 5:   {lista_notas[3]}':<100}")
    print(f"{f'Notas de 1:   {lista_notas[4]}':<100}")
    print("=" * 28)

main()
    