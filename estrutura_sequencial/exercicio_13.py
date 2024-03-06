#13-Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
    # Para homens: (72.7*h) - 58
    # Para mulheres: (62.1*h) - 44.7

def verifica_entrada(pergunta):
    while True:
        try:
            n = float(input(pergunta))
            if(0 <= n < 3):
                return n
            else:
                print("Verifique os valores digitados.")
        except Exception:
            print("Você deve digitar um número!")

print("Esse programa informa seu peso ideal baseado em sua altura e seu sexo.")
print("-" * 50)

sexo = verifica_entrada("Digite seu sexo(m = 0|f = 1): ")
altura = verifica_entrada("Digite sua altura(m): ")

if(sexo == 0):
    peso_ideal = (72.7 * altura) - 58
else:
    peso_ideal = (62.1 * altura) - 44.7

print("-" * 50)
print(f"Seu peso ideal é de {peso_ideal:.2f} kg.")