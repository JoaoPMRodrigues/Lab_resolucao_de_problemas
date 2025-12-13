n = int(input())
alfabeto = "abcdefghijklmnopqrstuvwxyz"
alfabeto = alfabeto.upper()
for i in range(n):
    letras = str(input())
    passos = int(input())
    codigo = ""
    for letra in letras:
        posicao = alfabeto.index(letra)
        if (posicao-passos) < 0:
            codigo += alfabeto[posicao-passos+26]
        else:
            codigo += alfabeto[posicao-passos]
    print(codigo)