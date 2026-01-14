L, C, M, N = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(L)]

# Prefix sum 2D simples
ps = [[0]*(C+1) for _ in range(L+1)]

for i in range(1, L+1):
    for j in range(1, C+1):
        ps[i][j] = (
            mat[i-1][j-1] 
            + ps[i-1][j] 
            + ps[i][j-1] 
            - ps[i-1][j-1]
        )

max_soma = -float("inf")

# Varre todas submatrizes M×N
for i in range(L - M + 1):
    for j in range(C - N + 1):
        i2, j2 = i + M, j + N
        soma = ps[i2][j2] - ps[i][j2] - ps[i2][j] + ps[i][j]
        max_soma = max(max_soma, soma)

print(max_soma)
