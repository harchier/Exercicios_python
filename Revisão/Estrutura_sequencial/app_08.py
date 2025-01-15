#08-Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valor_hora = float(input("Digite o quanto você ganha por hora (R$): "))

horas_trabalhadas_mes = float(input("Digite a quantidade de horas trabalhadas no mês (h): "))

salario = valor_hora * horas_trabalhadas_mes

print("-" * 100)
print(f"Salário = {salario} R$")

