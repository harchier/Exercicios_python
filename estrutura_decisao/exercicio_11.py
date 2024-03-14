#11-As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
	# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
	# salários até R$ 280,00 (incluindo) : aumento de 20%
	# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
	# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
	# salários de R$ 1500,00 em diante : aumento de 5% 
#Após o aumento ser realizado, informe na tela:
	# o salário antes do reajuste;
	# o percentual de aumento aplicado;
	# o valor do aumento;
	# o novo salário, após o aumento.

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_entrada(pergunta):
    while True:
        try:
            entrada = float(input(pergunta))
            if(entrada > 0):
                return entrada
            else:
                print("A entrada deve ser maior que zero.")
        except Exception:
            print("A entrada deve ser um número.")

def main():
    cabecalho('Esse programa calcula reajustes salariais de acordo com o salário.')

    salario = verifica_entrada("Digite o salário(R$): ")

    if(salario <= 280):
        percentual = "20 %"
        reajuste = 0.2
    elif(280 < salario <= 700):
        percentual = "15 %"
        reajuste = 0.15
    elif(700 < salario <= 1500):
        percentual = "10 %"
        reajuste = 0.10
    else:
        percentual = "5 %"
        reajuste = 0.05
    
    aumento = salario * reajuste
    novo_salario = salario + aumento

    print("=" * 100)
    print(f'''Salário antes         = R$ {salario}
Percentual de Aumento = {percentual}
Valor do aumento      = R$ {aumento}
Novo salário          = R$ {novo_salario}''')
    print("=" * 100)
main()
