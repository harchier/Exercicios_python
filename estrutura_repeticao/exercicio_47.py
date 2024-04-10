# 47-Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são informados ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
# 	Atleta: Aparecido Parente
# 	Nota: 9.9
# 	Nota: 7.5
# 	Nota: 9.5
# 	Nota: 8.5
# 	Nota: 9.0
# 	Nota: 8.5
# 	Nota: 9.7

# 	Resultado final:
# 	Atleta: Aparecido Parente
# 	Melhor nota: 9.9
# 	Pior nota: 7.5
# 	Média: 9,04

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
                print("A entrada deve ser um número entre 0 e 10.")
        except Exception:
            print("A entrada deve ser um número.")

def calcula_media():
    lista_a = []
    for e in range(7):
        nota = verifica_float(f"Nota {e + 1}: ")
        lista_a.append(nota)
    
    maior_nota = max(lista_a)
    menor_nota = min(lista_a)

    lista_b = lista_a[:]

    lista_b.remove(maior_nota)
    lista_b.remove(menor_nota)

    soma = 0
    for e in lista_b:
        soma += e
    
    media = soma / len(lista_b)

    return [maior_nota, menor_nota, media]

def main():
    cabecalho('Esse programa calcula a nota média de uma competição de ginástica.')

    total = 0
    melhor_media = 0
    campeao = 0
    while True:
        print(f"\nAtleta {total + 1}")
        nome = input("Nome: ")
        if(nome == ""):
            break
        else:
            resultado = calcula_media()
            if(resultado[2] > melhor_media):
                melhor_media = resultado[2]
                campeao = nome
            total += 1

            print("\nResultado final:")
            print(f"Atleta: {nome}")
            print(f"Melhor nota: {resultado[0]}")
            print(f"Pior nota: {resultado[1]}")
            print(f"Media: {resultado[2]:.2f}")
    
    print(f"\nTotal de atletas avaliados: {total}")
    print(f"Campeão: {campeao}")
    print(f"Melhor media: {melhor_media:.2f}")

main()