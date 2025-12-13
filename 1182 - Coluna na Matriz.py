coluna = int(input())
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
    soma += matriz[i][coluna]
    contador += 1

if operacao in "M":
    media = soma/contador
    print(f"{media:.1f}")
else:
    print(f"{soma:.1f}")
