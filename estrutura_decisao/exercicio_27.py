# 27-Uma fruteira está vendendo frutas com a seguinte tabela de preços:
# 	                      Até 5 Kg           Acima de 5 Kg
# 	Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# 	Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# 	Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

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

def calcula_preco(morango, maca):
    if(morango <= 5):
        valor_kg_mo = 2.5
    else:
        valor_kg_mo = 2.2
    
    if(maca <= 5):
        valor_kg_ma = 1.8
    else:
        valor_kg_ma = 1.5
    
    preco = (morango * valor_kg_mo) + (maca * valor_kg_ma)
    
    if((morango + maca) > 8) or (preco > 25):
        desconto = preco * 0.1
        preco = preco - desconto
    return preco

def main():
    cabecalho('Esse programa calcula o valor a ser pago em um banca de frutas.')

    morango = verifica_entrada("Digite a quantidade de morangos(Kg): ")
    maca = verifica_entrada("Digite a quantidade de maçãs(Kg): ")

    preco = calcula_preco(morango, maca)

    print("=" * 100)
    print(f"{f'Preço = {preco:.2f}':^100}")
    print("=" * 100)

main()