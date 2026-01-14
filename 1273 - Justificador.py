primeiro = True
while True:
    n = int(input())
    if n == 0:
        break
        #Para evitar apresentation error
    if not primeiro:
        print()
    primeiro = False
    nomes = []
    for i in range(n):
        nomes.append(str(input().strip()))
    # Vendo qual a maior palavra
    maior = len(nomes[0])
    for i in range(n):
        if len(nomes[i]) > maior:
            maior = len(nomes[i])
    # Justificando
    for i in range(len(nomes)):
        dif = maior - len(nomes[i])
        print(" "*dif + f"{nomes[i]}")
