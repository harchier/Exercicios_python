#19-Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
	# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
	# 326 = 3 centenas, 2 dezenas e 6 unidades
	# 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_entrada(pergunta):
    while True:
        try:
            entrada = int(input(pergunta))
            if(0 < entrada < 1000):
                return entrada
            else:
                print("A entrada deve ser maior que zero e menor que mil.")
        except Exception:
            print("A entrada deve ser um número.")

def main():
    cabecalho('Esse programa informa quantas centenas, dezenas e unidades possui um número menor que 1000.')
    
    n = verifica_entrada("Digite um número: ")
    
    centenas = n // 100
    resto_c = n % 100
    dezenas = resto_c // 10
    resto_d = resto_c % 10
    unidades = resto_d
    
    print("=" * 35)
    if(centenas > 1):
        if(dezenas > 1):
            if(unidades > 1):
                print(f"{centenas} centenas, {dezenas} dezenas e {unidades} unidades.")
            elif(unidades == 1):
                print(f"{centenas} centenas, {dezenas} dezenas e {unidades} unidade.")
            else:
                print(f"{centenas} centenas e {dezenas} dezenas.")
        elif(dezenas == 1):
            if(unidades > 1):
                print(f"{centenas} centenas, {dezenas} dezena e {unidades} unidades.")
            elif(unidades == 1):
                print(f"{centenas} centenas, {dezenas} dezena e {unidades} unidade.")
            else:
                print(f"{centenas} centenas e {dezenas} dezena.")
        else:
            if(unidades > 1):
                print(f"{centenas} centenas e {unidades} unidades.")
            elif(unidades == 1):
                print(f"{centenas} centenas e {unidades} unidade.")
            else:
                print(f"{centenas} centenas.")
    elif(centenas == 1):
        if(dezenas > 1):
            if(unidades > 1):
                print(f"{centenas} centena, {dezenas} dezenas e {unidades} unidades.")
            elif(unidades == 1):
                print(f"{centenas} centena, {dezenas} dezenas e {unidades} unidade.")
            else:
                print(f"{centenas} centena e {dezenas} dezenas.")
        elif(dezenas == 1):
            if(unidades > 1):
                print(f"{centenas} centena, {dezenas} dezenas e {unidades} unidades.")
            elif(unidades == 1):
                print(f"{centenas} centena, {dezenas} dezenas e {unidades} unidade.")
            else:
                print(f"{centenas} centena e {dezenas} dezenas.")
        else:
            if(unidades > 1):
                print(f"{centenas} centena e {unidades} unidades.")
            elif(unidades == 1):
                print(f"{centenas} centena e {unidades} unidade.")
            else:
                print(f"{centenas} centena.")
    else:
        if(dezenas > 1):
            if(unidades > 1):
                print(f"{dezenas} dezenas e {unidades} unidades.")
            elif(unidades == 1):
                print(f"{dezenas} dezenas e {unidades} unidade.")
            else:
                print(f"{dezenas} dezenas.")
        elif(dezenas == 1):
            if(unidades > 1):
                print(f"{dezenas} dezena e {unidades} unidades.")
            elif(unidades == 1):
                print(f"{dezenas} dezena e {unidades} unidade.")
            else:
                print(f"{dezenas} dezena.")
        else:
            if(unidades > 1):
                print(f"{unidades} unidades.")
            elif(unidades == 1):
                print(f"{unidades} unidade.")
    print("=" * 35)

while True:
    main()
