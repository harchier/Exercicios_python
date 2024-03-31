# 30-O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:
# 	Preço do pão: R$ 0.18
# 	Panificadora Pão de Ontem - Tabela de preços
# 	1 - R$ 0.18
# 	2 - R$ 0.36
# 	...
# 	50 - R$ 9.00

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
                print("A entrada deve ser maior que 0.")
        except Exception:
            print("A entrada deve ser um número.")

def verifica_quantidade(pergunta):
     while True:
        try:
            entrada = int(input(pergunta))
            if(entrada > 0):
                return entrada
            else:
                print("A entrada deve ser maior que 0.")
        except Exception:
            print("A entrada deve ser um número.")

def monta_tabela(quantidade, preco):
    i = 1
    while(i <= quantidade):
        print(f"{i:02d} - R$ {preco * i:.2f}")
        i += 1

def main():
    cabecalho('Esse programa monta uma tabela de acordo com o preço de um produto.')

    quantidade = verifica_quantidade("Digite a quantidade de produtos: ")

    preco = verifica_entrada("Digite o preço do produto: ")

    print("=" * 100)
    monta_tabela(quantidade, preco)
    print("=" * 100)

main()