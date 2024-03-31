# 29-O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que contém o número de itens que o cliente comprou e ao lado o valor da conta. Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços. Você foi contratado para desenvolver o programa que monta esta tabela de preços, que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo:
# 	Lojas Quase Dois - Tabela de preços
# 	1 - R$ 1.99
# 	2 - R$ 3.98
# 	...
# 	50 - R$ 99.50

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_entrada(pergunta):
    while True:
        try:
            entrada = float(input(pergunta))
            if(entrada > 0):
                return entrada
            else:
                print("O preço do produto deve ser maior que 0.")
        except Exception:
            print("O preço deve ser um número.")

def verifica_quantidade(pergunta):
    while True:
        try:
            entrada = int(input(pergunta))
            if(entrada > 0):
                return entrada
            else:
                print("A quantidade deve ser maior que 0.")
        except Exception:
            print("A quantidade deve ser um número inteiro.")

def monta_tabela(quantidade):
    lista = []
    for i in range(quantidade):
        preco = verifica_entrada(f"Digite o preço do produto {i + 1}: ")
        lista.append(preco)
    return lista

def imprime_lista(lista):
    for i,e in enumerate(lista):
        print(f"{i + 1} - R$ {e}")

def main():
    cabecalho('Esse programa monta uma tabela de preço.')
    
    quantidade = verifica_quantidade("Digite o número de produtos: ")

    lista = monta_tabela(quantidade)

    print("=" * 100)
    imprime_lista(lista)
    print("=" * 100)

main()