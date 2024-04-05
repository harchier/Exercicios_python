# 38-Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
# 	Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
# 	Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
# 	A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. 
# 	Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_entrada_float(pergunta):
    while True:
        try:
            entrada = float(input(pergunta))
            if(entrada > 0):
                return entrada
            else:
                print("A entrada deve ser maior que 0.")
        except Exception:
            print("A entrada deve ser um número.")

def verifica_entrada_int(pergunta):
    while True:
        try:
            entrada = int(input(pergunta))
            if(entrada > 0):
                return entrada
            else:
                print("A entrada deve ser maior que 0.")
        except Exception:
            print("A entrada deve ser um número inteiro.")

def verifica_ano_final(pergunta, ano_inicial):
    while True:
        try:
            entrada = int(input(pergunta))
            if(entrada > 0) and (entrada > ano_inicial):
                return entrada
            else:
                print("A entrada deve ser maior que 0.")
                print("O ano final deve ser maior que o inicial.")
        except Exception:
            print("A entrada deve ser um número inteiro.")

def calcula_aumento(salario, taxa, ano_inicial, ano_final):
    taxa = taxa / 100
    while(ano_inicial <= ano_final):
        aumento = salario * taxa
        salario += aumento
        taxa *= 2
        ano_inicial += 1
    return salario

def main():
    cabecalho('Esse programa calcula um salário com taxa de aumento variável ao longo dos anos.')

    salario = verifica_entrada_float("Digite o salário inicial: ")

    taxa = verifica_entrada_float("Digite a taxa de aumento(%)")

    ano_inicial = verifica_entrada_int("Digite o ano inicial: ")

    ano_final = verifica_ano_final("Digite o ano final: ", ano_inicial)

    salario_final = calcula_aumento(salario, taxa, ano_inicial, ano_final)

    print("=" * 100)
    print(f"Salario final = {salario_final:.2f}")
    print("=" * 100)

main()
