#3-Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

def verifica_entrada(pergunta):
    while True:
        try:
            entrada = input(pergunta) .lower()
            if(entrada == "f"):
                print("F - Feminino")
                return entrada
            elif(entrada == "m"):
                print("M - Masculino")
                return entrada
            else:
                print("Sexo Inválido.")
        except Exception:
            print("Erro, verifique as entradas.")

print("-" * 100)
print(f"{'Esse programa é uma função que verifica o sexo digitado.':^100}")
print("-" * 100)

teste = verifica_entrada("Digite seu sexo(m/f): ")