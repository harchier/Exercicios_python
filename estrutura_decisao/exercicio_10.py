#10-Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_turno():
    while True:
        entrada = input("Qual turno você estuda?(M/V/N): ").lower().strip()
        if(entrada == "m") or (entrada == "v") or (entrada == "n"):
            return entrada
        else:
            print("Valor inválido!")

def main():
    cabecalho('Esse programa mostra mensagens de acordo com seu turno de estudo.')
    
    turno = verifica_turno()
    
    if(turno == "m"):
        mensagem = "Bom dia!"
    elif(turno == "v"):
        mensagem = "Boa tarde!"
    else:
        mensagem = "Boa noite!"

    print("=" * 100)
    print(f"{f'{mensagem}':^100}")
    print("=" * 100)

main()