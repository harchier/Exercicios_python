#15-A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

def cabecalho(texto):
    print("-" * 100)
    print(f"{f'{texto}':^100}")
    print("-" * 100)

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

def gera_fibonacci(quantidade):
    if(quantidade == 1):
        lista = [1]
    elif(quantidade == 2):
        lista = [1, 1]
    else:
        lista = [1, 1]
        i = 0
        a = 1
        b = 1
        while(i <= (quantidade - 3)):
            c = a + b
            lista.append(c)
            a = b
            b = c
            i += 1
    return lista

def main():
    cabecalho('Esse programa gera a sequência de Fibonacci.')

    quantidade = verifica_quantidade("Digite quantos termos deve ter a sequência: ")

    lista = gera_fibonacci(quantidade)
    print("=" * 100)
    print(f"Fibonacci até {quantidade} : {lista}")
    print("=" * 100)

main()