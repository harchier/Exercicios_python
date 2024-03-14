#13-Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_entrada(pergunta):
    while True:
        try:
            entrada = int(input(pergunta))
            if(0 < entrada <= 7):
                return entrada
            else:
                print("A entrada deve ser um número entre 1 e 7. ")
        except Exception:
            print("A entrada deve ser um número.")

def main():
    cabecalho('Esse programa mostra um dia da semana correspondente a um número inteiro.')

    dias_semana = ["Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado"]

    dia = verifica_entrada("Digite um número inteiro de 1 a 7:")

    print("=" * 100)
    print(f"{dias_semana[dia - 1]:^100}")
    print("=" * 100)

main()