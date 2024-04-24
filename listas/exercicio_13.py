#13-Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

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
            print("A temperatura deve ser um número.")

def monta_lista():
    lista = []
    i = 1
    while(i <= 12):
        temp = verifica_float(f"Digite a temperatura media do mês {i}(°C): ")
        lista.append(temp)
        i += 1
    return lista

def calcula_media(lista):
    soma = 0
    for e in lista:
        soma += e
    media = soma / len(lista)
    return media

def numero_para_meses(lista):
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    meses_acima_media = []
    for e in lista:
        meses_acima_media.append(meses[e])
    return meses_acima_media
    

def main():
    cabecalho('Esse programa calcula a media anual das temperaturas.')

    lista = monta_lista()

    media = calcula_media(lista)

    meses_acima_media = []
    temp_acima_media = []
    i = 0
    while(i < len(lista)):
        if(lista[i] > media):
            meses_acima_media.append(i)
            temp_acima_media.append(lista[i])
        i += 1
    
    meses_extenso = numero_para_meses(meses_acima_media)

    print("=" * 100)
    print(f"Media = {media:.2f}°C")
    j = 0
    while(j < len(temp_acima_media)):
        print(f"{meses_extenso[j]} - {temp_acima_media[j]}°C", end=" ")
        j += 1
    print()
    print("=" * 100)

main()