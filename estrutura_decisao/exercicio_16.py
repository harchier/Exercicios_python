#16-Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
	# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
	# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
	# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
	# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

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

def monta_equacao(a, b, c):
    if(a != 0):
        if(b > 0):
            if(c > 0):
                print(f"{a}x² + {b}x + {c} = 0")
            elif(c == 0):
                print(f"{a}x² + {b}x = 0")
            else:
                print(f"{a}x² + {b}x {c} = 0")
        elif(b == 0):
            if(c > 0):
                print(f"{a}x² + {c} = 0")
            elif(c == 0):
                print(f"{a}x² = 0")
            else:
                print(f"{a}x² {c} = 0")
        else:
            if(c > 0):
                print(f"{a}x² {b}x + {c} = 0")
            elif(c == 0):
                print(f"{a}x² {b}x = 0")
            else:
                print(f"{a}x² {b}x {c} = 0")
    else:
        print()

def main():
    cabecalho('Esse programa calcula o conjunto solução de uma equação do 2º grau.')
    print("ax² + bx + c = 0")
    a = verifica_entrada("Digite o valor de a: ")
    b = verifica_entrada("Digite o valor de b: ")
    c = verifica_entrada("Digite o valor de c: ")
    print()
    monta_equacao(a,b,c)
    
    print("=" * 37)
    if(a == 0):
        print("A equação não é do 2º grau.")
    else:
        delta = (b**2) - (4 * a * c)
        if(delta < 0):
            print("Não há soluções reais para a equação.")
        elif(delta == 0):
            x = -b / 2 * a
            print(f"S = [{x}]")
        else:
            x1 = (-b + (delta ** (1/2))) / 2 * a
            x2 = (-b - (delta ** (1/2))) / 2 * a
            print(f"S = [{x2:.2f},{x1:.2f}]")
    print("=" * 37)


main()