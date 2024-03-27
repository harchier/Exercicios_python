#25-Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

def cabecalho(texto):
    print("-" * 100)
    print(f"{texto:^100}")
    print("-" * 100)

def verifica_entrada(pergunta):
    while True:
        try:
            entrada = int(input(pergunta))
            if(entrada > 0):
                return entrada
            else:
                print("A entrada deve ser um número maior que 0.")
        except Exception:
            print("A entrada deve ser um número inteiro.")

def gera_lista(n):
    lista = []
    for i in range(n):
        idade = verifica_entrada(f"Digite a idade da {i + 1}ª pessoa: ")
        lista.append(idade)
    return lista

def calcula_media(lista):
    soma = 0
    for e in lista:
        soma += e
    media = soma / len(lista)
    return media

def main():
    cabecalho('Esse programa calcula a idade média de um grupo de pessoas.')

    tamanho_grupo = verifica_entrada("Digite o número de pessoas: ")

    lista = gera_lista(tamanho_grupo)

    media = calcula_media(lista)

    if(0 < media <= 25):
        tipo = "Jovem"
    elif(25 < media <= 60):
        tipo = "Adulta"
    else:
        tipo = "Idosa"
    
    print("=" * 100)
    print(f"Media da turma = {media:.2f}")
    print(f"A turma é {tipo}.")
    print("=" * 100)

main()        

