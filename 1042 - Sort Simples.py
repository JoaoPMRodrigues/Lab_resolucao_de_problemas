lista = list(map(int, input().split()))
lista.sort()
reverso = sorted(lista, reverse=True)
for numero in lista:
    print(numero)

print()
for numero in reverso:
    print(numero)
