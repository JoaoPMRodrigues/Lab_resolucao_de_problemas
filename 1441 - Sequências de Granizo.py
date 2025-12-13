while True:
    n = int(input())
    if n == 0:
        break

    atual = n
    maior = atual

    while atual != 1:
        if atual % 2 == 0:
            atual = atual // 2
        else:
            atual = 3 * atual + 1

        if atual > maior:
            maior = atual

    print(maior)
