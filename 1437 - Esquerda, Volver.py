direcao = ["N", "O", "S", "L"]
while True:
    n = int(input())
    if n == 0:
        break
    comandos = str(input())
    final = 0
    for comando in comandos:
        if comando == "D":
            final -= 1
        else:
            final += 1
    print(direcao[final % 4])
