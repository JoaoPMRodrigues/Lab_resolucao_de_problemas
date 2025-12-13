n = int(input())
frases = []
for i in range(n):
    frases.append(list(map(str, input().split())))
for frase in frases:
    for palavra in frase:
        for letra in palavra:
            print(letra, end="")
            break
    print()
