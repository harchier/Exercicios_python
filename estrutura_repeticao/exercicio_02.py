#2-Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

def cabecalho(texto):
    print("-" * 100)
    print(f"{f'{texto}':^100}")
    print("-" * 100)

def verifica_senha(pergunta, usuario):
    while True:
        senha = input(pergunta)
        if(senha != usuario):
            return senha
        else:
            print("A senha deve ser diferente do nome de usuário.")

def main():
    cabecalho('Esse programa verifica se a senha é igual ao nome de usuário.')

    usuario = input("Digite o nome de usuário: ")
    senha = verifica_senha("Digite a senha: ", usuario)

    print("=" * 28)
    print("Usuário e senha confirmados.")
    print("=" * 28)

main()
