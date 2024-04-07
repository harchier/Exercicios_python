# 41-Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
# 	Os juros e a quantidade de parcelas seguem a tabela abaixo:
# 	Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
# 	1                                       0
# 	3                                       10
# 	6                                       15
# 	9                                       20
# 	12                                      25
# 	Exemplo de saída do programa:
# 	Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
# 	R$ 1.000,00     0               1                       R$  1.000,00
# 	R$ 1.100,00     100             3                       R$    366,00
# 	R$ 1.150,00     150             6                       R$    191,67


def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

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

def main():
    cabecalho('Esse programa monta uma tabela de acordo com uma dívida.')
    
    v = verifica_float("Digite o valor da dívida: ")
    print(f"XX{'Valor da dívida':^15} | {'Valor do juros':^15} | {'Quantidade de parcelas':^25} | {'Valor da parcela':^20}")
    for i in range(0,15,3):
        if(i == 0):
            tx = 0
        elif(i == 3):
            tx = 10 / 100
        elif(i == 6):
            tx = 15 / 100
        elif(i == 9):
            tx = 20 / 100
        else:
            tx = 25 / 100
        juros = v * tx
        valor_divida = v + juros
        if(i == 0):
            q_parcela = 1
        else:
            q_parcela = i
        valor_parcela = valor_divida / q_parcela

        print(f"R${valor_divida:^15} | {juros:^15.2f} | {q_parcela:^25} | {valor_parcela:^20.2f}")


main()
