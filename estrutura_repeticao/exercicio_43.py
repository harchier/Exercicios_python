# 43-O cardápio de uma lanchonete é o seguinte:
# 	Especificação   Código  Preço
# 	Cachorro Quente 100     R$ 1,20
# 	Bauru Simples   101     R$ 1,30
# 	Bauru com ovo   102     R$ 1,50
# 	Hambúrguer      103     R$ 1,20
# 	Cheeseburguer   104     R$ 1,30
# 	Refrigerante    105     R$ 1,00
# 	Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def mosta_cardapio():
    print("""Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00
"""+"-" * 100)

def verifica_pedido(pergunta):
    lista = [100, 101, 102, 103, 104, 105]
    while True:
        try:
            pedido = int(input(pergunta))
            if(pedido in lista):
                return pedido
            else:
                print("Pedido inválido. Verifique o número do pedido.")
        except Exception:
            print("Pedido inválido. O pedido deve ser um número inteiro.")

def verifica_quantidade(pergunta):
    while True:
        try:
            quantidade = int(input(pergunta))
            if(quantidade > 0):
                return quantidade
            else:
                print("A quantidade deve ser maior que 0.")
        except Exception:
            print("A quantidade deve ser um número inteiro.")

def main():
    cabecalho('Lanchonete do Bino.')
    
    d = {100:1.2, 101:1.3, 102:1.5, 103:1.2, 104:1.3, 105:1}
    i = 1
    total = 0
    while True:
        mosta_cardapio()
        pedido = verifica_pedido(f"Digite o código do seu {i}º pedido: ")
        quantidade = verifica_quantidade("Digite a quantidade: ")
        preco = d[pedido]
        valor_pedido = preco * quantidade
        total += valor_pedido
        print("-" * 100)
        print(f"Total do pedido {i}: R$ {valor_pedido:.2f}")
        print("-" * 100)
        mais_pedido = input("Deseja fazer outro pedido?(s/n): ")
        mais_pedido = mais_pedido.lower()
        if(mais_pedido == "n"):
            break
        i += 1
    
    print("=" * 100)
    print(f"Total a pagar: R$ {total:.2f}")
    print("=" * 100)

main()
