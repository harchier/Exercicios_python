#12-Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula:    (72.7*altura) - 58

def verifica_entrada(pergunta):
    while True:
        try:
            n = float(input(pergunta))
            if(0 < n < 3):
                return n
            else:
                print("A altura deve ser em metros.")
        except Exception:
            print("Você deve digitar um número!")

print("Esse programa calcula o peso ideal de uma pessoa.")
print("-" * 50)

altura = verifica_entrada("Digite sua altura(m): ")
peso_ideal = (72.7 * altura) - 58

print("-" * 50)
print(f"O seu peso ideal é de {peso_ideal:.2f} kg")