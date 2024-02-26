#08-Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

print("Esse programa calcula o seu salário com base nas horas trabalhadas.")
print("-" * 50)

valor_hora = float(input("Digite o quanto você ganha por hora(R$): "))
horas = int(input("Digite quantas horas você trabalhou esse mês: "))

salario = valor_hora * horas

print("-" * 50)
print(f"Salário = R${salario}")