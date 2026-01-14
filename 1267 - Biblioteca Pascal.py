while True:
    n, d = map(int, input().split())
    if n == d == 0:
        break
    jantares = list()
    for i in range(d):
        linha = list(map(int, input().split()))
        jantares.append(linha[:])
    for i in range(len(jantares[i])):
        boole = False
        if jantares[0][i] == 1:
            boole = True
            for j in range(len(jantares)):
                if jantares[0][i] != jantares[j][i]:
                    boole = False
                    break
        else:
            continue
        if boole:
            print("yes")
            break
    if not boole:
        print("no")
