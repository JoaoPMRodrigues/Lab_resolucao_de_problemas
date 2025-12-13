def verifica_par(jogador1, jogador2, jogada1, jogada2):
    soma = jogada1+jogada2
    if (soma) % 2 == 0:
        return jogador1
    else:
        return jogador2


vencedor = []
jogo = []
cnt = 1
while True:
    n = int(input())
    if n == 0:
        break
    jogador1 = str(input())
    jogador2 = str(input())
    for i in range(n):
        jogada1, jogada2 = map(int, input().split())
        vencedor.append(verifica_par(jogador1, jogador2, jogada1, jogada2))
    jogo.append(vencedor[:])
    vencedor.clear()
for partida in jogo:
    print(f"Teste {cnt}")
    for jogador in partida:
        print(jogador)
    print()
    cnt += 1
