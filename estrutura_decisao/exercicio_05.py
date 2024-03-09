#5-Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
	# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
	# A mensagem "Reprovado", se a média for menor do que sete;
	# A mensagem "Aprovado com Distinção", se a média for igual a dez.

def verifica_entrada(pergunta):
    while True:
        try:
            entrada = float(input(pergunta))
            if(0 <= entrada <= 10):
                return entrada
            else:
                print("A entrada deve ser um número entre 0 e 10.")
        except Exception:
            print("A entrada deve ser um número.")

print("-" * 100)
print(f"{'Esse programa calcula a média de um aluno':^100}")
print("-" * 100)

n1 = verifica_entrada("Digite a 1ª nota: ")
n2 = verifica_entrada("Digite a 2ª nota: ")

media = (n1 + n2) / 2
print("=" * 23)
if(media < 7):
    print("Reprovado.")
elif(7 <= media < 10):
    print("Aprovado.")
else:
    print("Aprovado com Distinção.")
print("=" * 23)