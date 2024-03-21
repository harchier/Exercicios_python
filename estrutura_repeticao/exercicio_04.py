#4-Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

def cabecalho(texto):
    print("-" * 100)
    print(f"{f'{texto}':^100}")
    print("-" * 100)

def main():
    cabecalho('Esse programa calcula o tempo necessário para duas populações se igualem.')
    
    b = 200000
    a = 80000
    ano = 0
    while(a != b):
        taxa_a = 0.03
        taxa_b = 0.015
        crescimento_a = a * taxa_a
        crescimento_b = b * taxa_b
        a += crescimento_a
        b += crescimento_b
        ano += 1
    
    print("=" * 100)
    print(f"{f'Serão necessários {ano} anos.':^100}")
    print("=" * 100)

main()