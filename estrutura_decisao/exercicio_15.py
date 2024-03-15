#15-Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
	# Dicas:
	# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
	# Triângulo Equilátero: três lados iguais;
	# Triângulo Isósceles: quaisquer dois lados iguais;
	# Triângulo Escaleno: três lados diferentes;

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_entrada(pergunta):
    while True:
        try:
            entrada = float(input(pergunta))
            if(entrada > 0):
                return entrada
            else:
                print("A entrada deve ser um número maior que zero.")
        except Exception:
            print("A entrada deve ser um número.")

def main():
    cabecalho('Esse programa informa se três lados podem formar um triângulo.')

    l1 = verifica_entrada("Digite o 1º lado: ")
    l2 = verifica_entrada("Digite o 2º lado: ")
    l3 = verifica_entrada("Digite o 3º lado: ")

    if((l1 + l2)> l3) and ((l2 + l3) > l1) and ((l1 + l3) > l2):
        e_triangulo = True
        if(l1 == l2 == l3):
            tipo = "Equilátero"
        elif(l1 == l2) or (l1 == l3) or (l2 == l3):
            tipo = "Isóceles"
        else:
            tipo = "Escaleno"
    else:
        e_triangulo = False
    
    print("=" * 100)
    if(e_triangulo == True):
        print(f"{f'Os lados formam um triângulo {tipo}.':^100}")
    else:
        print(f"{'Os lados não formam um triângulo.':^100}")
    print("=" * 100)

main()
    
