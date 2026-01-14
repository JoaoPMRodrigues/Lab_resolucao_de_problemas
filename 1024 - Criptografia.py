n = int(input())
for _ in range(n):
    texto = input()
    passo1 = ""
    for c in texto:
        if c.isalpha():
            passo1 += chr(ord(c) + 3)
        else:
            passo1 += c

    passo2 = passo1[::-1]

    metade = len(passo2) // 2
    resultado = ""

    for i in range(len(passo2)):
        if i >= metade:
            resultado += chr(ord(passo2[i]) - 1)
        else:
            resultado += passo2[i]

    print(resultado)
