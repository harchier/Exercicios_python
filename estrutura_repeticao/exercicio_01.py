# 1-Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

def cabecalho(texto):
    print("-" * 100)
    print(f"{f'{texto}':^100}")
    print("-" * 100)

def verifica_entrada(pergunta):
    while True:
        try:
            entrada = float(input(pergunta))
            if(0 <= entrada <= 10):
                return entrada
            else:
                print("A etrada deve ser um valor entre 0 e 10.")
        except Exception:
            print("A entrada deve ser um número.")

def main():
    cabecalho('Esse programa verifica se uma entrada é válida.')

    nota = verifica_entrada("Digite uma nota de 0 a 10: ")
    
    print("=" * 100)
    print(f"{f'{nota} é um valor válido!':^100}")
    print("=" * 100)

main()