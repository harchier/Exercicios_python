#14-Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# 	a."Telefonou para a vítima?"
# 	b."Esteve no local do crime?"
# 	c."Mora perto da vítima?"
# 	d."Devia para a vítima?"
# 	e."Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_resposta(pergunta):
    respostas = ["s", "S", "sim", "Sim", "n", "N", "não", "Não"]
    while True:
        entrada = input(pergunta)
        if(entrada in respostas):
            return entrada
        else:
            print("Resposta inválida, tente novamente.")

def calcula_classificação(n):
    if(n < 2):
        classificação = "Inocente"
    elif(n == 2):
        classificação = "Suspeito(a)"
    elif(n == 3) or (n == 4):
        classificação = "Cúmplice"
    else:
        classificação = "Assassino(a)"
    return classificação

def faz_pergunta():
    n_classificacao = 0
    repostas_positivas = ["s", "S", "sim", "Sim"]
    perguntas = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?" ]
    for e in perguntas:
        resposta = verifica_resposta(e)
        if(resposta in repostas_positivas):
            n_classificacao += 1
    return n_classificacao

def main():
    cabecalho('Esse programa verifica suspeitos')

    n_classificacao = faz_pergunta()

    classificacao = calcula_classificação(n_classificacao)

    print("=" * 100)
    print(f"Classificação = {classificacao}")
    print("=" * 100)

main()
        
