while True:
    n, q = map(int, input().split())
    if n == q == 0:
        break
    lista_dados = list()
    lista_procura = list()
    boole = [0]*q
    contador = 1
    for _ in range(n):
        lista_dados.append(int(input()))
    for _ in range(q):
        lista_procura.append(int(input()))

    for i in range(len(q)):
        for j in range(len(n)):
            if lista_procura[i] == lista_dados[q]:
                boole[i] = j+1
                break
    print(f"CASE# {contador}:")
    for i in range(len(boole)):
        if boole[i] == 0:
            print(f"{lista_procura[i]} not found")
        else:
            print(f"{lista_procura[i]} found at {boole[i]}")
    contador += 1
