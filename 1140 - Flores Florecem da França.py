while True:
    frase = list(map(str, input().upper().split()))
    if frase[0][0] == "*":
        break
    boole = True
    aux = frase[0][0]
    for letra in frase:
        if letra[0] != aux:
            boole = False
    if boole:
        print("Y")
    else:
        print("N")
