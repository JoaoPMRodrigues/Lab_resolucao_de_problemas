while True:
    try:
        n = int(input())
        convidados = list(map(int, input().split()))
        convidados.sort()
        cheio = len(convidados)//2
        meio = cheio
        maior_tempo = abs(convidados[meio]-convidados[meio-1])
        print(cheio, maior_tempo)
    except EOFError:
        break
