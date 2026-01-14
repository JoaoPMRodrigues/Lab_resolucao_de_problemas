operacao = str(input().upper())
matriz = list()
tamanho = 12
for i in range(tamanho):
    linha = []
    for j in range(tamanho):
        linha.append(float(input()))
    matriz.append(linha[:])
soma = contador = 0
for i in range(tamanho):
    for j in range(tamanho):
        if j < i:
            contador += 1
            soma += matriz[i][j]

if operacao in "M":
    media = soma/contador
    print(f"{media:.1f}")
else:
    print(f"{soma:.1f}")
