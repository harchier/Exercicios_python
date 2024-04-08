# 44-Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
# 	1 , 2, 3, 4  - Votos para os respectivos candidatos 
# 	(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
# 	5 - Voto Nulo
# 	6 - Voto em Branco
# 	Faça um programa que calcule e mostre:
# 	O total de votos para cada candidato;
# 	O total de votos nulos;
# 	O total de votos em branco;
# 	A percentagem de votos nulos sobre o total de votos;
# 	A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_int(pergunta):
    while True:
        try:
            entrada = int(input(pergunta))
            if(0 <= entrada <= 6):
                return entrada
            else:
                print("Entrada inválida.")
        except Exception:
            print("A entrada deve ser um número inteiro.")

def mostra_candidatos():
    print("""Candidatos disponíveis:
Candidato A - 1
Candidato B - 2
Candidato C - 3
Candidato D - 4
Nulo        - 5
Branco      - 6""")

def computa_votos():
    a = 0
    b = 0
    c = 0
    d = 0
    nulo = 0
    branco = 0
    total = 0
    while True:
        print("-" * 100)
        mostra_candidatos()
        print("-" * 100)
        voto = verifica_int("Digite o seu voto: ")
        if(voto == 0):
            print("Fim da votação!")
            break
        elif(voto == 1):
            a += 1
        elif(voto == 2):
            b += 1
        elif(voto == 3):
            c += 1
        elif(voto == 4):
            d += 1
        elif(voto == 5):
            nulo += 1
        elif(voto == 6):
            branco += 1
        total += 1
    return [a, b, c, d, nulo, branco, total]

def verifica_vencedor(lista, candidatos):
    v = []
    
    maior = max(lista)
    i = 0
    while(i <= 3):
        if(lista[i] == maior):
            v.append(i)
        i += 1

    print("=" * 100)
    if(len(v) > 1):
        print("Empatados:")
        for e in v:
            print(f"Candidato {candidatos[e]}")
    else:
        print(f"Vencedor: Candidato {candidatos[v[0]]}")
    print("=" * 100)

def main():
    cabecalho('Simulador de eleição.')
    c = ["A", "B", "C", "D"]
    votos = computa_votos()
    
    votos_candidatos = []
    for e in range(4):
        votos_candidatos.append(votos[e])
    
    verifica_vencedor(votos_candidatos, c)

    p_nulo = (votos[4] * 100) / votos[6]
    p_branco = (votos[5] * 100) / votos[6]

    
    for i in range(4):
        print(f"Candidato {c[i]}                  = {votos_candidatos[i]}")
    print(f"Nulos                        = {votos[4]}")
    print(f"Brancos                      = {votos[5]}")
    print(f"Porcentagem de votos nulos   = {p_nulo:.2f} %")
    print(f"Porcentagem de votos brancos = {p_branco:.2f} %")
    

main()
    
        
