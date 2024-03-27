#26-Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

def cabecalho(texto):
    print("-" * 100)
    print(f"{texto:^100}")
    print("-" * 100)

def verifica_n_eleitores(pergunta):
    while True:
        try:
            entrada = int(input(pergunta))
            if(entrada > 0):
                return entrada
            else:
                print("A entrada deve ser um número maior que 0.")
        except Exception:
            print("A entrada deve ser um número inteiro.")

def verifica_voto(pergunta, n_candidatos):
    while True:
        try:
            voto = int(input(pergunta))
            if(voto in n_candidatos):
                return voto
            else:
                print("O número digitado não corresponde a um candidato.")
        except Exception:
            print("A entrada deve ser um número.")

def imprime_lista_candidatos(nome_candidatos, n_candidatos):
    print("*" * 100)
    for e in range(len(n_candidatos)):
        print(f"{n_candidatos[e]}-{nome_candidatos[e]}")
    print("*" * 100)

def inicia_votacao(n_eleitores, nome_candidatos, n_candidatos):
    bolsonaro = 0
    lula = 0
    ciro = 0
    for i in range(n_eleitores):
        imprime_lista_candidatos(nome_candidatos, n_candidatos)
        voto = verifica_voto("Digite seu voto: ", n_candidatos)
        if(voto == 22):
            bolsonaro += 1
            print(f"Você votou no Bolsonaro.")
            print("=" * 100)
        elif(voto == 13):
            lula += 1
            print(f"Você votou no Lula.")
            print("=" * 100)
        else:
            print(f"Você votou no Ciro.")
            print("=" * 100)
            ciro += 1
    return [bolsonaro, lula, ciro]

def verifica_vencedor(lista):
    maior = lista[0]
    for e in lista:
        if(e > maior):
            maior = e
    if((maior == lista[0]) and (maior == lista[1])) or ((maior == lista[1]) and (maior == lista[2])) or ((maior == lista[0]) and (maior == lista[2])) or ((lista[0] == lista[1] == lista[2])):
        vencedor = "Segundo Turno"
    else:    
        if(maior == lista[0]):
            vencedor = "Bolsonaro"
        elif(maior == lista[1]):
            vencedor = "Lula"
        else:
            vencedor = "Ciro"
    return vencedor

def main():
    cabecalho('Esse program simula uma eleição entre três candidatos.')

    n_candidatos =[22, 13, 12]
    nome_candidatos = ["Bolsonaro", "Lula", "Ciro"]

    n_eleitores = verifica_n_eleitores("Digite o número de eleitores: ")

    votos = inicia_votacao(n_eleitores, nome_candidatos, n_candidatos)

    vencedor = verifica_vencedor(votos)

    print(f"Resultado:")
    print(f"Bolsonaro = {votos[0]}")
    print(f"Lula = {votos[1]}")
    print(f"Ciro = {votos[2]}")
    print("=" * 100)
    print(f"Vencedor = {vencedor}")

main()

