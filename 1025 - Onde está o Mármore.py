def busca_binaria(lista, procura):
    inicio = 0
    fim = len(lista)-1
    posicao = None

    while inicio <= fim:
        meio = (inicio + fim)//2
        if lista[meio] == procura:
            posicao = meio
            fim = meio - 1
        elif lista[meio] < procura:
            inicio = meio + 1
        else:
            fim = meio - 1
    return posicao


contador = 1

while True:
    n, q = map(int, input().split())
    if n == q == 0:
        break

    lista_dados = list()
    lista_procura = list()
    boole = list()

    for _ in range(n):
        lista_dados.append(int(input()))
    for _ in range(q):
        lista_procura.append(int(input()))

    lista_dados.sort()
    for i in range(len(lista_procura)):
        boole.append(busca_binaria(lista_dados, lista_procura[i]))

    print(f"CASE# {contador}:")
    for i in range(len(boole)):
        if boole[i] == None:
            print(f"{lista_procura[i]} not found")
        else:
            print(f"{lista_procura[i]} found at {boole[i]+1}")
    contador += 1
