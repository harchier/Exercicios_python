# 26-Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# 	Álcool:
# 	até 20 litros, desconto de 3% por litro
# 	acima de 20 litros, desconto de 5% por litro
# 	Gasolina:
# 	até 20 litros, desconto de 4% por litro
# 	acima de 20 litros, desconto de 6% por litro 
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

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

def verifica_combustivel():
    while True:
        combustivel = input("Digite o combustível(A/G): ")
        combustivel = combustivel.lower()
        if(combustivel == "a") or (combustivel == "g"):
            return combustivel
        else:
            print("Combustível inválido.")

def main():
    cabecalho('Esse programa simula descontos em um posto de gasolina')

    litros = verifica_entrada("Digite a quantidade de litros vendidos: ")
    combustivel = verifica_combustivel()
    if(combustivel == "a"):
        preco_litro = 1.9 
        if(litros <= 20):
            desconto = 0.03
        else:
            desconto = 0.05
    else:
        preco_litro = 2.5
        if(litros <= 20):
            desconto = 0.04
        else:
            desconto = 0.06
    
    valor_desconto = preco_litro * desconto
    valor_litro = preco_litro - valor_desconto
    valor_total = valor_litro * litros

    print("=" * 100)
    print(f"{f'Valor a ser pago = R$ {valor_total:.2f}':^100}")
    print("=" * 100)

main()