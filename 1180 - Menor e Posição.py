n = int(input())
lista = list(map(int, input().split()))
menor, menor_posicao = lista[0], 0

for i in range(1, len(lista)-1):
    if lista[i] < menor:
        menor = lista[i]
        menor_posicao = i

print(f"Menor valor: {menor}")
print(f"Posicao: {menor_posicao}")
