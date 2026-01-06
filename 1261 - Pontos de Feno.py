dicionario = dict()
descricao = list()
m, n = map(int, input().split())

for _ in range(m):
    skill, valor = map(str, input().split())
    valor = float(valor)
    dicionario[skill] = valor

for _ in range(n):
    total = 0
    while True:
        linha = str(input())
        if linha == ".":
            break
        linha = linha.split()
        for i in range(len(linha)):
            if linha[i] in dicionario:
                total += dicionario[linha[i]]
    print(int(total))
