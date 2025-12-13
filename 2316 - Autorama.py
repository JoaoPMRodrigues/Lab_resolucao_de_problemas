k, n, m = map(int, input().split())

esperado = [1] * (n + 1)
contagem = [0] * (n + 1)
tempo_ultimo = [-1] * (n + 1)

for t in range(m):
    x, y = map(int, input().split())

    if y == esperado[x]:
        contagem[x] += 1
        tempo_ultimo[x] = t

        if esperado[x] < k:
            esperado[x] += 1
        else:
            esperado[x] = 1
    else:
        pass

ranking = []
for i in range(1, n + 1):
    ranking.append((-contagem[i], tempo_ultimo[i], i))

ranking.sort()
print(" ".join(str(x[2]) for x in ranking))
