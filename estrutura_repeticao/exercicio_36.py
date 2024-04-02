# 36-Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:
# 	Montar a tabuada de: 5
# 	Começar por: 4
# 	Terminar em: 7

# 	Vou montar a tabuada de 5 começando em 4 e terminando em 7:
# 	5 X 4 = 20
# 	5 X 5 = 25
# 	5 X 6 = 30
# 	5 X 7 = 35
# 	Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_entrada(pergunta):
    while True:
        try:
            entrada = int(input(pergunta))
            if(entrada >= 0):
                return entrada
            else:
                print("A entrada deve ser maior ou igual a zero.")
        except Exception:
            print("A entrada deve ser um número inteiro.")

def verifica_final(pergunta, comeco):
    while True:
        try:
            final = int(input(pergunta))
            if(final > comeco):
                return final
            else:
                print("O valor final deve ser maior que o inicial.")
        except Exception:
            print("O valor final deve ser um número inteiro.")

def monta_tabuada(n, comeco, final):
    j = comeco
    while(j <= final):
        print(f"{n} x {j} = {n * j}")
        j += 1
        

def main():
    cabecalho('Esse programa monta uma tabuada.')

    n = verifica_entrada("Montar a tabuada de: ")
    comeco = verifica_entrada("Começar por: ")
    final = verifica_final("Terminar em: ", comeco)
    
    print("=" * 100)
    monta_tabuada(n, comeco, final)
    print("=" * 100)

main()
