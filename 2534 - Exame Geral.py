while True:
    try:
        n, q = map(int, input().split())
        notas = list()
        for _ in range(n):
            notas.append(int(input()))
        notas.sort(reverse=True)
        for _ in range(q):
            pos = int(input())
            print(notas[pos-1])
    except EOFError:
        break
