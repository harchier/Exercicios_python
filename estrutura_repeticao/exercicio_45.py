# 45-Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
# 	Maior e Menor Acerto;
# 	Total de Alunos que utilizaram o sistema;
# 	A Média das Notas da Turma.
# 	Gabarito da Prova:

# 	01 - A
# 	02 - B
# 	03 - C
# 	04 - D
# 	05 - E
# 	06 - E
# 	07 - D
# 	08 - C
# 	09 - B
# 	10 - A
# 	Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_questao(pergunta):
    lista = ["A", "B", "C", "D", "E"]
    while True:
        entrada = input(pergunta)
        entrada = entrada.upper()
        if(entrada in lista):
            return entrada
        else:
            print("A entrada deve ser uma letra (A,B,C,D,E)")

def define_gabarito():
    g = []
    for e in range(10):
        questao = verifica_questao(f"Digite o gabarito da questão {e + 1}: ")
        g.append(questao)
    print("\n" * 20)
    return g

def main():
    cabecalho('Simulador de Gabarito.')

    gabarito = define_gabarito()

    maior_acerto = 0
    menor_acerto = float('inf')
    total = 0
    soma_acertos = 0
    while True:
        acertos = 0
        for e, i in enumerate(gabarito):
            resposta = verifica_questao(f"Digite a resposta do exercício {e + 1}: ")
            resposta = resposta.upper()
            if(resposta == i):
                acertos += 1
        if(acertos > maior_acerto):
            maior_acerto = acertos
        if(acertos < menor_acerto):
            menor_acerto = acertos
        soma_acertos += acertos
        total += 1

        print("-" * 100)
        print(f"Acertos = {acertos}")
        print("-" * 100)

        outro_uso = input("Outro aluno usará o sistema?(s/n): ")
        outro_uso = outro_uso.lower()
        if(outro_uso == "n"):
            print("Fim da avaliação.")
            break
    media = soma_acertos / total

    print("=" * 100)
    print(f"Maior acerto: {maior_acerto}")
    print(f"Menor acerto: {menor_acerto}")
    print(f"Total de alunos: {total}")
    print(f"Media da turma: {media:.2f}")
    print(f"Gabarito.")
    for e, i in enumerate(gabarito):
        print(f"{e + 1} - {i}",end="| ")
    print()
    print("=" * 100)

main()