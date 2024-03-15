#18-Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def divide_data(pergunta):
    while True:
        try:
            entrada = input(pergunta)
            entrada_dividida = entrada.split("/")
            lista = []
            for e in entrada_dividida:
                e = int(e)
                lista.append(e)
            return lista
        except Exception:
            print("A entrada deve ser um número.")

def verifica_bissexto(ano):
    if(ano % 4 == 0):
        if(ano % 100 == 0):
            if(ano % 400 == 0):
                bissexto = True
            else:
                bissexto = False
        else:
            bissexto = True
    else:
        bissexto = False
    return bissexto

def verifica_data(lista):
    meses_30 = [4,6,9,11]
    
    try:
        dia = lista[0]
        mes = lista[1]
        ano = lista[2]
        ano_bissexto = verifica_bissexto(ano)
        if(ano_bissexto == True):
            if(1 <= mes <= 12):
                if(mes == 2):
                    if(1 <= dia <= 29):
                        data_valida = True
                    else:
                        data_valida = False
                elif(mes in meses_30):
                    if(1 <= dia <= 30):
                        data_valida = True
                    else:
                        data_valida = False
                else:
                    if(1 <= dia <= 31):
                        data_valida = True
                    else:
                        data_valida = False
            else:
                data_valida = False
        else:
            if(1 <= mes <= 12):
                if(mes == 2):
                    if(1 <= dia <= 28):
                        data_valida = True
                    else:
                        data_valida = False
                elif(mes in meses_30):
                    if(1 <= dia <= 30):
                        data_valida = True
                    else:
                        data_valida = False
                else:
                    if(1 <= dia <= 31):
                        data_valida = True
                    else:
                        data_valida = False
            else:
                data_valida = False
    except IndexError:
        data_valida = False
    return data_valida

def main():
    cabecalho('Esse programa verifica se uma data é válida.')
    
    lista = divide_data("Digite uma data: ")
    data_valida = verifica_data(lista)

    print("=" * 100)
    if(data_valida == True):
        print(f"{'Data válida':^100}")
    else:
        print(f"{'Data inválida':^100}")
    print("=" * 100)

main()