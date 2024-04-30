# 16-Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
# a.$200 - $299
# b.$300 - $399
# c.$400 - $499
# d.$500 - $599
# e.$600 - $699
# f.$700 - $799
# g.$800 - $899
# h.$900 - $999
# i.$1000 em diante
# Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_quantidade(pergunta):
    while True:
        try:
            entrada = int(input(pergunta))
            if(entrada > 0):
                return entrada
            else:
                print("A entrada deve ser maior que zero.")
        except Exception:
            print("A entrada deve ser um número.")

def verifica_venda(pergunta):
    while True:
        try:
            entrada = float(input(pergunta))
            if(entrada >= 0):
                return entrada
            else:
                print("O valor da entrada deve ser maior ou igual a zero.")
        except Exception:
            print("A entrada deve ser um número.")

def calcula_salario():
    venda = verifica_venda("Digite o valor da venda semanal: ")
    salario = 200 + (venda * 0.09)
    return salario

def atribui_tabela(n):
    lista = []
    i = 0
    while(i < n):
        print(f"{i + 1}º vendedor: ")
        salario = calcula_salario()
        print("-" * 100)
        lista.append(salario)
        i += 1
    return lista

def conta_lista(lista):
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0
    i = 0
    for x in lista:
        if(200 <= x <= 299):
            a += 1
        elif(300 <= x <= 399):
            b += 1
        elif(400 <= x <= 499):
            c += 1
        elif(500 <= x <= 599):
            d += 1
        elif(600 <= x <= 699):
            e += 1
        elif(700 <= x <= 799):
            f += 1
        elif(800 <= x <= 899):
            g += 1
        elif(900 <= x <= 999):
            h += 1
        else:
            i += 1
    return [a, b, c, d, e, f, g, h, i]
        
        
def main():
    cabecalho('Relação de vendas.')

    n = verifica_quantidade("Digite o número de vendedores: ")

    lista = atribui_tabela(n)
    
    contadores = conta_lista(lista)

    print("=" * 100)
    print("Salário semanal dos vendedores.")
    print(f"$200-299 = {contadores[0]}")
    print(f"$300-399 = {contadores[1]}")
    print(f"$400-499 = {contadores[2]}")
    print(f"$500-599 = {contadores[3]}")
    print(f"$600-699 = {contadores[4]}")
    print(f"$700-799 = {contadores[5]}")
    print(f"$800-899 = {contadores[6]}")
    print(f"$900-999 = {contadores[7]}")
    print(f"$1000 em diante = {contadores[8]}")
    print("=" * 100)

main()

