#15-Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
    # salário bruto.
    # quanto pagou ao INSS.
    # quanto pagou ao sindicato.
    # o salário líquido.
    # calcule os descontos e o salário líquido, conforme a tabela abaixo:
    # + Salário Bruto : R$
    # - IR (11%) : R$
    # - INSS (8%) : R$
    # - Sindicato ( 5%) : R$
    # = Salário Liquido : R$
    # Obs.: Salário Bruto - Descontos = Salário Líquido.
def verifica_entrada(pergunta):
    while True:
        try:
            entrada = float(input(pergunta))
            if(entrada > 0):
                return entrada
            else:
                print("O valor de entrada não pode ser negativo.")
        except Exception:
            print("O valor de entrada deve ser um número maior que 0.")

print("-" * 100)
print(f"{'Esse programa calcula o salário baseado nas horas trabalhadas e o valor/hora.':^100}")
print("-" * 100)

valor_hora = verifica_entrada("Digite o valor/hora(R$): ")
horas_trabalhadas = verifica_entrada("Digite o número de horas trabalhadas: ")

salario_bruto = valor_hora * horas_trabalhadas
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - ir - inss - sindicato

print("=" * 50)
print(f"""+ Salário Bruto :   R$ {salario_bruto}
- IR (11%) :        R$ {ir}
- INSS (8%) :       R$ {inss}
- Sindicato ( 5%) : R$ {sindicato}
= Salário Liquido : R$ {salario_liquido}
""")