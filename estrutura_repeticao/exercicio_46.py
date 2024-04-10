# 46-Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média). Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são ordenados. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
# 	Atleta: Rodrigo Curvêllo

# 	Primeiro Salto: 6.5 m
# 	Segundo Salto: 6.1 m
# 	Terceiro Salto: 6.2 m
# 	Quarto Salto: 5.4 m
# 	Quinto Salto: 5.3 m

# 	Melhor salto:  6.5 m
# 	Pior salto: 5.3 m
# 	Média dos demais saltos: 5.9 m

# 	Resultado final:
# 	Rodrigo Curvêllo: 5.9 m

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_float(pergunta):
    while True:
        try:
            entrada = float(input(pergunta))
            if(entrada >= 0):
                return entrada
            else:
                print("A entrada deve ser um número positivo.")
        except Exception:
            print("A entrada deve ser um número.")

def calcula_media():
    lista = []
    salto_1 = verifica_float("Primeiro salto: ")
    lista.append(salto_1)
    salto_2 = verifica_float("Segundo salto: ")
    lista.append(salto_2)
    salto_3 = verifica_float("Terceiro salto: ")
    lista.append(salto_3)
    salto_4 = verifica_float("Quarto salto: ")
    lista.append(salto_4)
    salto_5 = verifica_float("Quinto salto: ")
    lista.append(salto_5)
    
    maior_salto = max(lista)
    menor_salto = min(lista)

    print("-" * 100)
    print(f"Melhor salto: {maior_salto} m")
    print(f"Pior salto: {menor_salto} m")

    lista.remove(maior_salto)
    lista.remove(menor_salto)

    soma = 0
    for e in lista:
        soma += e
    media = soma / len(lista)

    print(f"Media dos demais saltos: {media:.2f} m")

    return media

def main():
    cabecalho('Esse programa calcula a resultado de uma competição de salto a distância.')

    campeao = 0
    maior_media = 0
    total = 0
    while True:
        nome = input("Nome: ")
        if(nome == ""):
            break
        else:
            media = calcula_media()
            if(media > maior_media):
                maior_media = media
                campeao = nome
            total += 1
        print("-" * 100)
    
    print(f"Resultado Final:\n{campeao}: {maior_media:.2f} m")

main()
    
  