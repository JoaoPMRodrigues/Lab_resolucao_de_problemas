l, c, m, n = map(int, input().split())
plantacao = list()
max = -float("inf")
for i in range(l):
    plantacao.append(list(map(int, input().split())))

for i in range(0, l, m):
    for j in range(0, c, n):
        s = 0
        for k in range(i, i+m):
            for p in range(j, j+n):
                s += plantacao[k][p]
        if s > max:
            max = s
print(max)
