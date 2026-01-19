n = int(input())

for _ in range(n):
    cartas = input().split()
    baralho = []

    for pos, carta in enumerate(cartas):
        valor, naipe = carta[0], carta[1]
        if valor == "T":
            v = 10
        elif valor == "J":
            v = 11
        elif valor == "Q":
            v = 12
        elif valor == "K":
            v = 13
        else:
            v = int(valor)

        naipe_valor = {"H": 0, "C": 1, "D": 2, "S": 3}[naipe]

        baralho.append({
            "valor": v,
            "naipe": naipe,
            "naipe_valor": naipe_valor,
            "posicao": pos
        })

    primeira = baralho[0]
    carta_naipe = primeira["naipe"]
    carta_valor = primeira["valor"]

    ordem_natural = sorted(baralho[1:], key=lambda c: (
        c["naipe_valor"], c["valor"]))
    apresentadas = baralho[1:]

    if apresentadas == [ordem_natural[0], ordem_natural[1], ordem_natural[2]]:
        total = 1
    elif apresentadas == [ordem_natural[0], ordem_natural[2], ordem_natural[1]]:
        total = 2
    elif apresentadas == [ordem_natural[1], ordem_natural[0], ordem_natural[2]]:
        total = 3
    elif apresentadas == [ordem_natural[1], ordem_natural[2], ordem_natural[0]]:
        total = 4
    elif apresentadas == [ordem_natural[2], ordem_natural[0], ordem_natural[1]]:
        total = 5
    else:
        total = 6

    carta_valor += total
    if carta_valor > 13:
        carta_valor -= 13

    if carta_valor == 10:
        valor_str = "T"
    elif carta_valor == 11:
        valor_str = "J"
    elif carta_valor == 12:
        valor_str = "Q"
    elif carta_valor == 13:
        valor_str = "K"
    else:
        valor_str = str(carta_valor)
        
    print(valor_str + carta_naipe)