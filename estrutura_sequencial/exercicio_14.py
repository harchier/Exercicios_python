#14-João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

def verifica_entrada(pergunta):
    while True:
        try:
            n = float(input(pergunta))
            if(n > 0):
                return n
            else:
                print("Verifique as entradas.")
        except Exception:
            print("A entrada deve ser um número.")

print("Esse programa verifica a multa a ser paga pelo excesso de pesca.")
print("-" * 50)

peso = verifica_entrada("Digite o peso dos peixes(kg): ")

print("-" * 50)
if(peso > 50):
    excesso = peso - 50
    multa = excesso * 4
    print(f"O peso pescado foi de {peso} kg.")
    print(f"O excesso foi de {excesso} kg.")
    print(f"A multa a ser paga será de R$ {multa}.")
else:
    print(f"Não há multa a ser paga, pois o peso {peso} kg não ultrapassa o limite de 50 kg.")

