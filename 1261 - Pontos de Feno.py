dicionario = dict()
descricao = list()
m, n = map(int, input().split())
for _ in range(m):
    skill, valor = map(str, input().split())
    valor = float(valor)
    dicionario[skill] = valor

for _ in range(n):
    frase = ""
    while True:
        linha = str(input())
        if linha == ".":
            break
        frase += linha
