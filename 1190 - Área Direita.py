operacao = str(input().upper())
matriz = list()
tamanho = 12
for i in range(tamanho):
    linha = list()
    for j in range(tamanho):
        linha.append(float(input()))
    matriz.append(linha[:])

soma = contador = 0
for i in range(tamanho):
    for j in range(tamanho):
        if i < j and i+j > tamanho - 1:
            soma += matriz[i][j]
            contador += 1

if operacao in "M":
    media = soma/contador
    print(f"{media:.1f}")
else:
    print(f"{soma:.1f}")