n, m = map(int, input().split())
tempo = list()
for i in range(n):
    rodadas = list(map(int, input().split()))
    tempo.append(rodadas[:])
posicao_primeiro = posicao_segundo = posicao_terceiro = -float("inf")
valor_primeiro = valor_segundo = valor_terceiro = float("inf")
for i in range(len(tempo)):
    if sum(tempo[i]) < valor_primeiro:
        posicao_terceiro, valor_terceiro = posicao_segundo, valor_segundo
        posicao_segundo, valor_segundo = posicao_primeiro, valor_primeiro
        posicao_primeiro, valor_primeiro = i+1, sum(tempo[i])
    elif sum(tempo[i]) < valor_segundo:
        posicao_terceiro, valor_terceiro = posicao_segundo, valor_segundo
        posicao_segundo, valor_segundo = i+1, sum(tempo[i])
    elif sum(tempo[i]) < valor_terceiro:
        posicao_terceiro, valor_terceiro = i+1, sum(tempo[i])

print(posicao_primeiro)
print(posicao_segundo)
print(posicao_terceiro)
