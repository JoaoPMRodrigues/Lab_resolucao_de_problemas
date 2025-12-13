contagem = []
maior = -float("inf")
while True:
    frase = str(input().strip())
    if frase == "0":
        break
    frase = frase.split()
    for palavra in frase:
        contagem.append(len(palavra))
    for i in range(len(contagem)):
        if contagem[i] >= maior:
            maior = contagem[i]
            maiorp = frase[i]

    for i in range(len(contagem)):
        if i != len(contagem)-1:
            print(contagem[i], end="-")
        else:
            print(contagem[i], end="")
    print()
    contagem.clear()
print()
print(f"The biggest word: {maiorp}")
