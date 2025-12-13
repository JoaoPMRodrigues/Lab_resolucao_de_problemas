n = int(input())
frase = []
for i in range(n):
    frase.append(str(input()))
for i in range(len(frase)):
    aux=set()
    for letra in frase[i]:
        if letra not in aux and letra.isalpha():
            aux.add(letra)
    if len(aux)==26:
        print("frase completa")
    elif 26>len(aux)>=13:
        print("frase quase completa")
    else:
        print("frase mal elaborada")