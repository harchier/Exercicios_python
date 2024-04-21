#6-Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_float(pergunta):
    while True:
        try:
            entrada = float(input(pergunta))
            if(0 <= entrada <= 10):
                return entrada
            else:
                print("A entrada deve estar entre 0 e 10.")
        except Exception:
            print("A entrada deve ser um número.")

def verifica_tamanho(pergunta):
    while True:
        try:
            entrada = int(input(pergunta))
            if(entrada > 0):
                return entrada
            else:
                print("A entrada deve ser maior que 0.")
        except Exception:
            print("A entrada deve ser um número inteiro.")

def calcula_media(n_notas, n_alunos):
    lista = []
    a = 1
    while(a <= n_alunos):
        n = 1
        soma = 0
        print(f"Aluno {a}:")
        while(n <= n_notas):
            nota = verifica_float(f"Digite a {n}ª nota: ")
            soma += nota
            n += 1
        print("-" * 100)
        media = soma / n_notas
        lista.append(media)
        a += 1
    return lista

def main():
    cabecalho('Esse programa calcula a media de 4 notas de 10 alunos.')

    n_notas = verifica_tamanho("Digite a quantidade de notas: ")
    n_alunos = verifica_tamanho("Digite o nº de alunos: ")

    medias = calcula_media(n_notas, n_alunos)

    aprovados = []
    for e in medias:
        if(e >= 7):
            aprovados.append(e)
    
    print("=" * 100)
    print(f"Medias = {medias}")
    print(f"Numero de alunos aprovados: {len(aprovados)}")
    print("=" * 100)

main()