#42-Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_float(pergunta):
    while True:
        try:
            entrada = float(input(pergunta))
            return entrada
        except Exception:
            print("A entrada deve ser um número.")

def main():
    cabecalho('Esse programa conta quantos números estão em intervalos determinados.')
    cabecalho('Intervalos: [0-25], [26-50], [51-75], [76-100]')
    cabecalho('Para sair digite um número negativo.')

    intervalo_1 = 0
    intervalo_2 = 0
    intervalo_3 = 0
    intervalo_4 = 0

    while True:
        n = verifica_float("Digite um número positivo: ")
        if(n < 0):
            break
        else:
            if(0 <= n <= 25):
                intervalo_1 += 1
            elif(26 <= n <= 50):
                intervalo_2 += 1
            elif(51 <= n <= 75):
                intervalo_3 += 1
            else:
                intervalo_4 += 1
    
    print("=" * 100)
    print(f"[0-25]   = {intervalo_1}")
    print(f"[26-50]  = {intervalo_2}")
    print(f"[51-75]  = {intervalo_3}")
    print(f"[76-100] = {intervalo_4}")
    print("=" * 100)

main()