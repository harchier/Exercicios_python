#24-Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
	# par ou ímpar;
	# positivo ou negativo;
	# inteiro ou decimal.

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_entrada(pergunta):
    while True:
        try:
            entrada = float(input(pergunta))
            return entrada   
        except Exception:
            print("A entrada deve ser um número.")

def verifica_operador(pergunta):
    while True:
        try:
            lista_operadores = ["+", "-", "*", "/", "**", "raiz"]
            operador = input(pergunta)
            if(operador in lista_operadores):
                return operador
            else:
                print("Operador não encontrado, verifique a lista de operadores.")
        except Exception:
            print("Ocorreu um erro, verifique as entradas.")            

def imprime_lista_operadores():
    print("""
====================================================
Operadores suportados
+ = Soma
- = Subtração
* = Multiplicação
/ = Divisão
** = Potenciação
raiz = Radicalização (2 raiz 4 = raiz quadrada de 4)
====================================================""")

def resultado_operacao(n1,op,n2):
    if(op == "+"):
        resultado = n1 + n2
    elif(op == "-"):
        resultado = n1 - n2
    elif(op == "*"):
        resultado = n1 * n2
    elif(op == "**"):
        resultado = n1 ** n2
    elif(op == "/"):
        resultado = n1 / n2
    elif(op == "raiz"):
        resultado = n2 ** (1/n1)
    return resultado

def e_par(n):
    if(n % 2 == 0):
        par = True
    else:
        par = False
    return par

def e_positivo(n):
    if(n > 0):
        positivo = True
    else:
        positivo = False
    return positivo

def e_inteiro(n):
    if(n % 1 == 0):
        inteiro = True
    else:
        inteiro = False
    return inteiro

def imprime_resultado(n1, op, n2, resultado, conceito_1, conceito_2, conceito_3):
    print("=" * 100)
    if(op == "+"):
        print(f"{f'{n1} + {n2} = {resultado}':^100}")
    elif(op == "-"):
        print(f"{f'{n1} - {n2} = {resultado}':^100}")
    elif(op == "*"):
        print(f"{f'{n1} * {n2} = {resultado}':^100}")
    elif(op == "**"):
        print(f"{f'{n1} ** {n2} = {resultado}':^100}")
    elif(op == "/"):
        print(f"{f'{n1} / {n2} = {resultado}':^100}")
    elif(op == "raiz"):
        print(f"{f'raiz {n1} de {n2} = {resultado}':^100}")
    print(f"{f'{conceito_1}, {conceito_2}, {conceito_3}':^100}")
    print("=" * 100)

def main():
    cabecalho('Esse programa realiza operações entre dois números.')
    
    lista_informativa = input("Deseja imprimir a lista informativa?(s/n)")
    if(lista_informativa == "s") or (lista_informativa == "S"):
        imprime_lista_operadores()
    
    n1 = verifica_entrada("Digite o 1º número: ")
    operador = verifica_operador("Digite um operador: ")
    n2 = verifica_entrada("Digite o 2º número: ")

    resultado = resultado_operacao(n1,operador,n2)
    par = e_par(resultado)
    if(par == True):
        conceito_1 = "Par"
    else:
        conceito_1 = "ímpar"
    if(resultado > 0):
        conceito_2 = "Positivo"
    elif(resultado == 0):
        conceito_2 = "Neutro"
    else:
        conceito_2 = "Negativo"
    inteiro = e_inteiro(resultado)
    if(inteiro == True):
        conceito_3 = "Inteiro"
    else:
        conceito_3 = "Decimal"

    imprime_resultado(n1, operador, n2, resultado, conceito_1, conceito_2, conceito_3)

main()
