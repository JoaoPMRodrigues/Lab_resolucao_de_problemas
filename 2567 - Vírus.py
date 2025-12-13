while True:
    try:
        n = int(input())
        virus = list(map(int, input().split()))
        virus.sort(reverse=True)
        soma = inicio = 0
        fim = len(virus)-1
        while inicio < fim:
            soma += (virus[inicio]-virus[fim])
            inicio += 1
            fim -= 1
        print(soma)
    except EOFError:
        break
