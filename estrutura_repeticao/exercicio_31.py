# 31-O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:
# 	Lojas Tabajara 
# 	Produto 1: R$ 2.20
# 	Produto 2: R$ 5.80
# 	Produto 3: R$ 0
# 	Total: R$ 9.00
# 	Dinheiro: R$ 20.00
# 	Troco: R$ 11.00
# 	...

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_entrada(pergunta):
    while True:
        try:
            entrada = float(input(pergunta))
            if(entrada >= 0):
                return entrada
            else:
                print("A entrada deve ser maior que 0.")
        except Exception:
            print("A entrada deve ser um número.")

def soma_produtos():
    soma = 0
    i = 1
    while True:
        p = verifica_entrada(f"Produto {i}: ")
        if(p == 0):
            break
        soma += p
        i += 1
    return soma

def verifica_dinheiro(pergunta, total):
    while True:
        try:
            dinheiro = float(input(pergunta))
            if(dinheiro >= total):
                return dinheiro
            else:
                print("O dinheiro fornecido deve ser maior ou igual ao total.")
        except Exception:
            print("O valor deve ser um número.")

def main():
    cabecalho('Lojas Tabajara')
    
    i = 1
    while True:
        print(f"Operação {i}")
        total = soma_produtos()
        print(f"Total: {total}")
        dinheiro = verifica_dinheiro("Dinheiro: ", total)
        troco = dinheiro - total
        print(f"Troco: {troco}")
        print("=" * 100)
        i += 1

main()