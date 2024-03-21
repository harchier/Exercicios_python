# 3-Faça um programa que leia e valide as seguintes informações:
# 	a.Nome: maior que 3 caracteres;
# 	b.Idade: entre 0 e 150;
# 	c.Salário: maior que zero;
# 	d.Sexo: 'f' ou 'm';
# 	e.Estado Civil: 's', 'c', 'v', 'd';

def cabecalho(texto):
    print("-" * 100)
    print(f"{f'{texto}':^100}")
    print("-" * 100)

def verifica_nome(pergunta):
    while True:
        nome = input(pergunta)
        if(len(nome) > 3):
            return nome
        else:
            print("O nome deve ter mais de 3 caracteres.")

def verifica_idade(pergunta):
    while True:
        idade = int(input(pergunta))
        if(0 < idade <= 150):
            return idade
        else:
            print("A idade deve ser entre 0 e 150.")

def verifica_salario(pergunta):
    while True:
        salario = int(input(pergunta))
        if(salario > 0):
            return salario
        else:
            print("O salário deve ser maior que 0.")

def verifica_sexo(pergunta):
    while True:
        sexo = input(pergunta)
        if(sexo == "f") or (sexo == "m"):
            return sexo
        else:
            print("O sexo deve ser 'f' ou 'm'.")

def verifica_estado_civil(pergunta):
    while True:
        estado_civil = input(pergunta)
        if(estado_civil == "s") or (estado_civil == "c") or (estado_civil == "v") or (estado_civil == "d"):
            return estado_civil
        else:
            print("O estado civil deve ser 's', 'c', 'v' ou 'd'.")

def main():
    cabecalho('Esse programa verifica se uma serie de dados são válidos.')

    nome = verifica_nome("Digite seu nome: ")
    idade = verifica_idade("Digite sua idade: ")
    salario = verifica_salario("Digite seu salário: ")
    sexo = verifica_sexo("Digite seu sexo(f/m): ")
    estado_civil = verifica_estado_civil("Digite seu estado civil(s/c/v/d): ")

    print("=" * 100)
    print(f"{f'Nome = {nome}':^100}")
    print(f"{f'Idade = {idade}':^100}")
    print(f"{f'Salário = {salario}':^100}")
    print(f"{f'Sexo = {sexo}':^100}")
    print(f"{f'Estado civil = {estado_civil}':^100}")
    print("=" * 100)

main()