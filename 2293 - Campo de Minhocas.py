l, c = map(int, input().split())
matriz = list()
for i in range(l):
    linha = list(map(int, input().split()))
    matriz.append(linha[:])
maiorL = maiorC = -float("inf")
soma = 0
for i in range(l):
    soma = sum(matriz[i])
    if soma > maiorL:
        maiorL = soma
for i in range(c):
    soma = 0
    for j in range(l):
        soma += matriz[j][i]
    if soma > maiorC:
        maiorC = soma

if maiorC >= maiorL:
    print(maiorC)
else:
    print(maiorL)

