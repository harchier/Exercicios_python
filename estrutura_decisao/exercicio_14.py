#14-Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#   Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 9.0         B
#   Entre 6.0 e 7.5         C
#   Entre 4.0 e 6.0         D
#   Entre 4.0 e zero        E
# 	O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_entrada(pergunta):
    while True:
        try:
            entrada = float(input(pergunta))
            if(0 < entrada <= 10):
                return entrada
            else:
                print("A entrada deve ser um número entre 0 e 10. ")
        except Exception:
            print("A entrada deve ser um número.")

def main():
    cabecalho('Esse programa calcula a media entre duas notas e atribui conceitos.')

    n1 = verifica_entrada("Digite a 1ª nota: ")
    n2 = verifica_entrada("Digite a 2ª nota: ")

    media = (n1 + n2) / 2

    if(media > 9):
        conceito = "A"
    elif(7.5 < media <= 9):
        conceito = "B"
    elif(6 < media <= 7.5):
        conceito = "C"
    elif(4 < media <= 6):
        conceito = "D"
    else:
        conceito = "E"
    
    aprovado = ["A", "B", "C"]

    if(conceito in aprovado):
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    print("=" * 100)
    print(f"{f'Nota 1 = {n1}, Nota 2 = {n2}, Media = {media}, Conceito = {conceito}, Situação = {situacao}':^100}")
    print("=" * 100)

main()