cnt = 1
while True:
    N = int(input().strip())
    if N == 0:
        break

    conjuntos = [set() for _ in range(6)]

    for i in range(N):
        arr = input().strip().split()
        nums, letras = arr[:10], arr[10:]

        mapeamento = {
            'A': (nums[0], nums[1]),
            'B': (nums[2], nums[3]),
            'C': (nums[4], nums[5]),
            'D': (nums[6], nums[7]),
            'E': (nums[8], nums[9])
        }

        for j in range(6):
            letra = letras[j]
            digito1, digito2 = mapeamento[letra]

            if i == 0:
                conjuntos[j] = {digito1, digito2}
            else:
                conjuntos[j] &= {digito1, digito2}

    senha = [sorted(conjuntos[j])[0] for j in range(6)]

    print(f"Teste {cnt}")
    print(" ".join(senha) + " ")
    print()

    cnt += 1
