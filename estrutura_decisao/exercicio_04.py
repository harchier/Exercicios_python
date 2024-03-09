#4-Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

print("-" * 100)
print(f"{'Esse programa verifica vogais e consoantes.':^100}")
print("-" * 100)

vogais = ["a", "e", "i", "o", "u"]
consoantes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

letra = input("Digite uma letra: ") .lower().strip()

print("=" * 100)
if(letra in vogais):
    print(f"{'É uma vogal.':^100}")
elif(letra in consoantes):
    print(f"{'É uma consoante.':^100}")
else:
    print(f"{'Caractere inválido.':^100}")
print("=" * 100)