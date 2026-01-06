dicionario = dict()
descricao = list()
m, n = map(int, input().split())
for _ in range(m):
    skill, valor = map(str, input().split())
    valor = float(valor)
    dicionario[skill] = valor

for _ in range(n):
    auxiliar = list()
    while True:
        linha = str(input())
        if linha == ".":
            break
        auxiliar.append(linha)
    descricao.append(auxiliar[:])

for i in range(len(descricao)):
    total = 0
    for palavra in descricao[i]:
        if palavra in dicionario:
            total += dicionario[palavra]
    print(total)
