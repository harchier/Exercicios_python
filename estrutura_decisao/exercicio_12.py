# 12-Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# 	Desconto do IR:
# 	Salário Bruto até 900 (inclusive) - isento
# 	Salário Bruto até 1500 (inclusive) - desconto de 5%
# 	Salário Bruto até 2500 (inclusive) - desconto de 10%
# 	Salário Bruto acima de 2500 - desconto de 20% 
#Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#         Salário Bruto: (5 * 220)        : R$ 1100,00
#         (-) IR (5%)                     : R$   55,00  
#         (-) INSS ( 10%)                 : R$  110,00
#         FGTS (11%)                      : R$  121,00
#         Total de descontos              : R$  165,00
#         Salário Liquido                 : R$  935,00

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
    cabecalho('Esse programa calcula uma folha de pagamento tendo como base o salário.')
    
    v_hora = verifica_entrada("Digite o valor da hora: ")
    n_horas = verifica_entrada("Digite o número de horas trabalhadas: ")

    salario_bruto = v_hora * n_horas

    if(salario_bruto <= 900):
        t_ir = 0
        imposto_renda = "0 %"
    elif(900 < salario_bruto <= 1500):
        t_ir = 0.05
        imposto_renda = "5 %"
    elif(1500 < salario_bruto <= 2500):
        t_ir = 0.1
        imposto_renda = "10 %"
    else:
        t_ir = 0.2
        imposto_renda = "20 %"
    
    ir = salario_bruto * t_ir

    inss = salario_bruto * 0.1

    fgts = salario_bruto * 0.11

    total_descontos = ir + inss

    salario_liquido = salario_bruto - total_descontos
    print("=" * 60)
    print(f"{f'Salário Bruto: ({v_hora} * {n_horas})    ':<45} : R$ {salario_bruto:>7.2f}")
    print(f"{f'(-) IR ({imposto_renda})                 ':<45} : R$ {ir:>7.2f}")
    print(f"{f'(-) INSS ( 10%)                          ':<45} : R$ {inss:>7.2f}")
    print(f"{f'FGTS (11%)                               ':<45} : R$ {fgts:>7.2f}")
    print(f"{f'Total de descontos                       ':<45} : R$ {total_descontos:>7.2f}")
    print(f"{f'Salário Liquido                          ':<45} : R$ {salario_liquido:>7.2f}")

    

main()