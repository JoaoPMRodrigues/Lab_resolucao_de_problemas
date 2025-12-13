n = int(input())
pares = list()
impares = list()
for i in range(n):
    numeros = int(input())

    if numeros % 2 == 0:
        pares.append(numeros)
    else:
        impares.append(numeros)

pares.sort()
impares.sort(reverse=True)
for i in range(len(pares)):
    print(pares[i])
for i in range(len(impares)):
    print(impares[i])
