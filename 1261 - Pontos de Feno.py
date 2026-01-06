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
    descricao.append(frase.split())

for i in range(len(descricao)):
    total = 0
    repetidos = set()
    for palavra in descricao[i]:
        if palavra in dicionario and palavra not in repetidos:
            total += dicionario[palavra]
            repetidos.add(palavra)
    print(int(total))
