while True:
    try:
        frase = input().upper().split()
        repetidas = 0
        i = 1
        while i < len(frase):
            if frase[i][0] == frase[i - 1][0]:
                repetidas += 1
                letra = frase[i][0]
                while i < len(frase) and frase[i][0] == letra:
                    i += 1
            else:
                i += 1
        print(repetidas)
    except EOFError:
        break