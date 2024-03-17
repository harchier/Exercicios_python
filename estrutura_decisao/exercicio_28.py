# 28-O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
# 	                      Até 5 Kg           Acima de 5 Kg
# 	File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# 	Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# 	Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# 	Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_quantidade(pergunta):
    while True:
        try:
            entrada = float(input(pergunta))
            if(entrada > 0):
                return entrada
            else:
                print("A entrada deve ser maior que 0.") 
        except Exception:
            print("A entrada deve ser um número.")

def verifica_tipo():
    while True:
        try:
            print("=" * 50)
            print(f"{f'Tipos de Carne':^50}")
            print("1- Filé duplo")
            print("2- Alcatra")
            print("3- Picanha")
            print("=" * 50)
            tipo = int(input("Escolha o tipo de carne: "))
            lista = []
            if(tipo == 1):
                nome_tipo = "Filé Duplo"
                lista.append(nome_tipo)
                lista.append(tipo)
                return lista
            elif(tipo == 2):
                nome_tipo = "Alcatra"
                lista.append(nome_tipo)
                lista.append(tipo)
                return lista
            elif(tipo == 3):
                nome_tipo = "Picanha"
                lista.append(nome_tipo)
                lista.append(tipo)
                return lista
            else:
                print("Tipo inválido.")
        except Exception:
            print("O tipo deve ser um número inteiro.")

def verifica_pagamento():
    while True:
        try:
            lista = []
            print("=" * 50)
            print(f"{f'Formas de Pagamento':^50}")
            print("1- Cartão Tabajara(desconto 5%)")
            print("2- Dinheiro")
            print("3- Pix")
            print("4- Cartão de crédito")
            print("=" * 50)
            pagamento = int(input("Digite a forma de pagamento: "))
            if(pagamento == 1):
                tipo_pagamento = "Cartão Tabajara."
            elif(pagamento == 2):
                tipo_pagamento = "Dinheiro."
            elif(pagamento == 3):
                tipo_pagamento = "Pix."
            elif(pagamento == 4):
                tipo_pagamento = "Cartão de crédito."
            else:
                print("Forma inválido.")
            lista.append(tipo_pagamento)
            lista.append(pagamento)
            return lista
        except Exception:
            print("A forma de pagamento deve ser um número inteiro.")

def verifica_preco(tipo, quantidade, forma_pagamento):
    if(tipo == 1):
        if(quantidade <= 5):
            preco_kg = 4.9
        else:
            preco_kg = 5.8
    elif(tipo == 2):
        if(quantidade <= 5):
            preco_kg = 5.9
        else:
            preco_kg = 6.8
    else:
        if(quantidade <= 5):
            preco_kg = 6.9
        else:
            preco_kg = 7.8
    
    lista = []
    preco_inicial = quantidade * preco_kg
    if(forma_pagamento == 1):
        valor_desconto = preco_inicial * 0.05
        preco_final = preco_inicial - valor_desconto
    else:
        preco_final = preco_inicial
    lista.append(preco_inicial)
    lista.append(preco_final)
    return lista

def imprime_cupom(tipo, quantidade, preco, forma_pagamento):
    print("=" * 50)
    print(f"{f'CUPOM FISCAL':^50}")
    print(f"{f'Tipo: {tipo[0]}':^50}")
    print(f"{f'Quantidade: {quantidade} Kg':^50}")
    print(f"{f'Tipo Pagamento: {forma_pagamento[0]}':^50}")
    print(f"{f'Preço inicial = {preco[0]:.2f}':^50}")
    if(forma_pagamento[1] == 1):
        print(f"{f'Desconto: 5%':^50}")
        print(f"{f'Valor a pagar: {preco[1]:.2f}':^50}")
    else:
        print(f"{f'Desconto: 0%':^50}")
        print(f"{f'Valor a pagar: {preco[0]:.2f}':^50}")
    print("=" * 50)

def main():
    cabecalho('Esse programa calcula o preço da carne.')

    tipo = verifica_tipo()
    quantidade = verifica_quantidade("Quantos kilos? ")
    forma_pagamento = verifica_pagamento()
    preco = verifica_preco(tipo[1], quantidade, forma_pagamento[1])

    imprime_cupom(tipo, quantidade, preco, forma_pagamento)

main()
            