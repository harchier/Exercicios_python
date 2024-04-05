# 37-Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_codigo(pergunta):
    while True:
        try:
            codigo = int(input(pergunta))
            if(codigo >= 0):
                return codigo
            else:
                print("O código deve ser igual ou maior que zero.")
        except Exception:
            print("O código deve ser um número inteiro.")

def verifica_entrada(pergunta):
    while True:
        try:
            entrada = float(input(pergunta))
            if(entrada > 0):
                return entrada
            else:
                print("A entrada deve ser maior que 0.")
        except Exception:
            print("A entrada deve ser um número.")

def main():
    cabecalho('Esse program faz um censo entre os clientes da academia.')

    n_clientes = 0

    soma_altura = 0
    soma_peso = 0

    maior_altura = 0
    codigo_maior_altura = 0
    
    maior_peso = 0
    codigo_maior_peso = 0
    
    menor_altura = float('inf')
    codigo_menor_altura = 0
    
    menor_peso = float('inf')
    codigo_menor_peso = 0
    while True:
        print(f"Cliente {n_clientes + 1}")
        codigo = verifica_codigo("Digite o codigo: ")
        if(codigo == 0):
            break
        altura = verifica_entrada("Digite a altura(cm): ")
        if(altura > maior_altura):
            maior_altura = altura
            codigo_maior_altura = codigo
        if(altura < menor_altura):
            menor_altura = altura
            codigo_menor_altura = codigo
        soma_altura += altura
        peso = verifica_entrada("Digite a massa(kg): ")
        if(peso > maior_peso):
            maior_peso = peso
            codigo_maior_peso = codigo
        if(peso < menor_peso):
            menor_peso = peso
            codigo_menor_peso = codigo
        soma_peso += peso
        n_clientes += 1
    
    media_altura = soma_altura / n_clientes
    media_peso = soma_peso / n_clientes
    
    print("=" * 100)
    print(f"Cliente mais alto: Código = {codigo_maior_altura} Altura = {maior_altura} cm")
    print(f"Cliente mais baixo: Código = {codigo_menor_altura} Altura = {menor_altura} cm")
    print(f"Cliente mais pesado: Código = {codigo_maior_peso} Peso = {maior_peso} Kg")
    print(f"Cliente mais leve: Código = {codigo_menor_peso} Peso = {menor_peso} Kg")
    print(f"Média das alturas: {media_altura} cm/cliente")
    print(f"Média das massas: {media_peso} Kg/cliente")
    print("=" * 100)

main()
