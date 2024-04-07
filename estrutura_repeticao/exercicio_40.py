# 40-Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
# 	Código da cidade;
# 	Número de veículos de passeio (em 1999);
# 	Número de acidentes de trânsito com vítimas (em 1999). 
#Deseja-se saber:
# 	Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
# 	Qual a média de veículos nas cinco cidades juntas;
# 	Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_numero_inteiro(pergunta):
    while True:
        try:
            numero = int(input(pergunta))
            if(numero >= 0):
                return numero
            else:
                print("A entrada deve ser maior ou igual a 0.")
        except Exception:
            print("A entrada deve ser um número inteiro.")

def main():
    cabecalho('Esse programa retorna dados estatísticos sobre veículos de cidades.')

    codigo_mais_acidente = 0
    maior_indice_acidente = 0
    
    codigo_menos_acidente = 0
    menor_indice_acidente = float('inf')
    
    soma_veiculos = 0
    soma_acidentes_menos_2000 = 0
    
    cidades_menos_2000 = 0
    
    for e in range(5):
        codigo = verifica_numero_inteiro(f"Digite o código da {e + 1}ª cidade: ")
        n_veiculos = verifica_numero_inteiro(f"Digite o número de veículos da cidade {codigo} em 1999: ")
        n_acidentes = verifica_numero_inteiro(f"Digite o número de acidentes com vítima da cidade {codigo} em 1999: ")
        soma_veiculos += n_veiculos
        if(n_veiculos < 2000):
            soma_acidentes_menos_2000 += n_acidentes
            cidades_menos_2000 += 1
        if(n_acidentes > maior_indice_acidente):
            codigo_mais_acidente = codigo
            maior_indice_acidente = n_acidentes
        if(n_acidentes < menor_indice_acidente):
            codigo_menos_acidente = codigo
            menor_indice_acidente = n_acidentes


    media_veiculos = soma_veiculos / 5
    media_acidentes_menos_2000 = soma_acidentes_menos_2000 / cidades_menos_2000
    
    print("=" * 100)
    print(f"Maior índice de acidentes: cidade {codigo_mais_acidente}, {maior_indice_acidente} acidentes.")
    print(f"Menor índice de acidentes: cidade {codigo_menos_acidente}, {menor_indice_acidente} acidentes.")
    print(f"Media de veículos por cidade: {media_veiculos}")
    print(f"Media de acidentes nas cidades com menos de 2000 veículos: {media_acidentes_menos_2000}")
    print("=" * 100)

main()