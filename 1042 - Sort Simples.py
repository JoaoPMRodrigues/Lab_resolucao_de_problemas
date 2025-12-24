lista = list(map(int, input().split()))
lista.sort()
for numero in lista:
    print(numero)

print()
for i in range(len(lista)-1, -1, -1):
    print(lista[i])
