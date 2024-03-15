#20-Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
	# A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
	# A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
	# A mensagem "Aprovado com Distinção", se a média for igual a 10.

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_entrada(pergunta):
    while True:
        try:
            entrada = float(input(pergunta))
            if(0 <= entrada <= 10):
                return entrada
            else:
                print("A entrada deve ser maior que zero e menor que dez.")
        except Exception:
            print("A entrada deve ser um número.")

def main():
    cabecalho('Esse programa calcula a média de um aluno entre três notas.')

    n1 = verifica_entrada("Digite a 1ª nota: ")
    n2 = verifica_entrada("Digite a 2ª nota: ")
    n3 = verifica_entrada("Digite a 3ª nota: ")

    media = (n1 + n2 + n3) / 3

    if(media < 7):
        situacao = "Reprovado"
    elif(7 <= media < 10):
        situacao = "Aprovado"
    else:
        situacao = "Aprovado com Distinção"
    
    print("=" * 100)
    print(f"{f'Media = {media:.2f} | Situação = {situacao}':^100}")
    print("=" * 100)

main()
