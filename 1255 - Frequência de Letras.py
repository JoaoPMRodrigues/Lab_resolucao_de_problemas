n = int(input())
contagem = []
letra = []
rsp = []
rspf = list()
for i in range(n):
    # Armazenando e tirando os espaços da frase
    frase = input().strip().lower()
    frase = frase.replace(" ", "")
    maior = -float("inf")
    # conta quantas vezes se repete cada letra
    for l in range(len(frase)):
        if frase[l].isalpha() and frase[l] not in letra:
            contagem.append(frase.count(frase[l]))
            letra.append(frase[l])

    # Separa as letras que mais se repetem
    for i in range(len(contagem)):
        if contagem[i] > maior:
            maior = contagem[i]
    for i in range(len(letra)):
        if contagem[i] == maior:
            rsp.append(letra[i])
    contagem.clear()
    letra.clear()
    # Organiza as respostas
    for i in range(len(rsp)):
        for j in range(i, len(rsp)):
            if rsp[i] > rsp[j]:
                rsp[i], rsp[j] = rsp[j], rsp[i]
    rspf.append(rsp[:])
    rsp.clear()
    # print no resultado
for palavra in rspf:
    for letra in palavra:
        print(letra, end="")
    print()
