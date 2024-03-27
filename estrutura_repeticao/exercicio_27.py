# 27-Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_turma(pergunta):
    while True:
        try:
            entrada = int(input(pergunta))
            if(entrada > 0):
                return entrada
            else:
                print("A entrada deve ser maior que 0.")
        except Exception:
            print("A entrada deve ser um número inteiro.")

def verifica_alunos(pergunta):
    while True:
        try:
            entrada = int(input(pergunta))
            if(0 < entrada <= 40):
                return entrada
            else:
                print("A entrada deve ser um número entre 1 e 40.")
        except Exception:
            print("A entrada deve ser um número inteiro.")

def soma_alunos(n_turmas):
    soma = 0
    for e in range(n_turmas):
        n_alunos = verifica_alunos(f"Digite o número de alunos da turma {e + 1}: ")
        soma += n_alunos
    return soma 

def calcula_media(n_turmas, n_alunos):
    media = n_alunos / n_turmas
    return media

def main():
    cabecalho('Esse programa calcula a media de alunos por turma.')

    n_turmas = verifica_turma("Digite a quantidade de turmas: ")

    n_alunos = soma_alunos(n_turmas)

    media = calcula_media(n_turmas, n_alunos)

    print("=" * 100)
    print(f"Media de alunos por turma = {media:.2f}")
    print("=" * 100)

main()

