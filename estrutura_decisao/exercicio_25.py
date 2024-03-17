# #25-Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# 	"Telefonou para a vítima?"
# 	"Esteve no local do crime?"
# 	"Mora perto da vítima?"
# 	"Devia para a vítima?"
# 	"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_entrada(pergunta):
    while True:
        try:
            entrada = int(input(pergunta))
            if(entrada == 0) or (entrada == 1):
                return entrada
            else:
                print("A entrada deve ser 0 ou 1.")   
        except Exception:
            print("A entrada deve ser um número.")

def main():
    cabecalho('Esse programa faz 5 perguntas para avaliar um possível suspeito.')

    classificacao = 0
    print("Responda as perguntas abaixo com 0-Não e 1-Sim.")
    p1 = verifica_entrada("Telefonou para a vítima? ")
    if(p1 == 1):
        classificacao += 1
    p2 = verifica_entrada("Esteve no local do crime? ")
    if(p2 == 1):
        classificacao += 1
    p3 = verifica_entrada("Mora perto da vítima? ")
    if(p3 == 1):
        classificacao += 1
    p4 = verifica_entrada("Devia para a vítima? ")
    if(p4 == 1):
        classificacao += 1
    p5 = verifica_entrada("Já trabalhou com a vítima? ")
    if(p5 == 1):
        classificacao += 1
    
    if(classificacao < 2):
        veredito = "Inocente"
    elif(classificacao == 2):
        veredito = "Suspeito"
    elif(2 < classificacao <=4 ):
        veredito = "Cúmplice"
    else:
        veredito = "Assassino"
    
    print("=" * 100)
    print(f"{f'Veredito: {veredito}':^100}")
    print("=" * 100)

main()