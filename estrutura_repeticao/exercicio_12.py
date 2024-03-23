#12-Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
# Tabuada de 5:
# 5 X 1 = 5
# 5 X 2 = 10
# ...
# 5 X 10 = 50

def cabecalho(texto):
    print("-" * 100)
    print(f"{f'{texto}':^100}")
    print("-" * 100)

def verifica_entrada(pergunta):
    while True:
        try:
            entrada = int(input(pergunta))
            return entrada
        except Exception:
            print("A entrada deve ser um número.")

def gera_tabuada(numero):
    print(f"Tabuada de {numero}:")
    i = 1
    while(i <= 10):
        print(f"{numero} X {i} = {numero * i}")
        i += 1

def main():
    cabecalho('Esse programa gera a tabuada de um número escolhido.')

    numero = verifica_entrada("Digite o número: ")

    print("=" * 100)
    gera_tabuada(numero)
    print("=" * 100)

main()