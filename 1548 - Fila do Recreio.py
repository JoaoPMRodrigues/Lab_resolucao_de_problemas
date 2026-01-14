n = int(input())
for i in range(n):
    m = int(input())
    lista_alunos = list(map(int, input().split()))
    lista_ordenada = sorted(lista_alunos, reverse=True)
    t = 0
    for i in range(len(lista_alunos)):
        if lista_alunos[i] == lista_ordenada[i]:
            t += 1
    print(t)
    lista_alunos.clear()
    lista_ordenada.clear()
