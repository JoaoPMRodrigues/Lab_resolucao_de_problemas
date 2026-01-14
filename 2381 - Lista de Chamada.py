n, k = map(int, input().split())
alunos = list()
for i in range(n):
    alunos.append(str(input()))
alunos.sort()
print(alunos[k-1])
