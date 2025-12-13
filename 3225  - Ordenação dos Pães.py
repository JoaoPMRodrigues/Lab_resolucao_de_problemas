n = int(input())
permutacao_inicial = list(map(int, input().split()))
permutacao_final = list(map(int, input().split()))
posicao = {valor: i for i, valor in enumerate(permutacao_inicial)}
vetor = [posicao[x] for x in permutacao_final]
aux = [0] * n
total_inversoes = 0
tamanho = 1

while tamanho < n:
    inicio = 0

    while inicio < n - tamanho:
        meio = inicio + tamanho
        fim = min(inicio + 2 * tamanho, n)
        i = inicio
        j = meio
        k = inicio

        while i < meio and j < fim:
            if vetor[i] <= vetor[j]:
                aux[k] = vetor[i]
                i += 1
            else:
                aux[k] = vetor[j]
                j += 1
                total_inversoes += meio - i
            k += 1

        while i < meio:
            aux[k] = vetor[i]
            i += 1
            k += 1

        while j < fim:
            aux[k] = vetor[j]
            j += 1
            k += 1

        for x in range(inicio, fim):
            vetor[x] = aux[x]
        inicio += 2 * tamanho
    tamanho *= 2

if total_inversoes % 2 == 0:
    print("Possible")
else:
    print("Impossible")
