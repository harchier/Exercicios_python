#18-Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

def verifica_entrada(pergunta):
    while True:
        try:
            entrada = float(input(pergunta))
            if(entrada > 0):
                return entrada
            else:
                print("O valor da entrada deve ser maior que zero.")
        except Exception:
            print("O valor da etrada deve ser um número.")

print("-" * 100)
print(f"{'Esse programa calcula o tempo de um download.':^100}")
print("-" * 100)

megabytes = verifica_entrada("Digite o tamanho do arquivo(Mb): ")
velocidade = verifica_entrada("Digite a velocidade da internet(Mbps): ")

megabits = megabytes * 8

segundos = megabits / velocidade 

horas = segundos // 3600
sobra_seg = segundos % 3600
min = sobra_seg // 60
seg = sobra_seg % 60

print("=" * 100)
print(f"O tempo será de {horas} h, {min} min e {seg} s.")
print("=" * 100)