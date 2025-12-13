t = 1

while True:
    A, V = map(int, input().split())
    if A == 0 and V == 0:
        break

    grau = [0] * (A + 1)

    for _ in range(V):
        x, y = map(int, input().split())
        grau[x] += 1
        grau[y] += 1

    maior = max(grau[1:])
    
    print(f"Teste {t}")
    for i in range(1, A + 1):
        if grau[i] == maior:
            print(i, end=" ")
    print("\n")

    t += 1