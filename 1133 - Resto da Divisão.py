def resto(inicio, fim):
    valores = list()
    for i in range(inicio+1, fim):
        if i % 5 == 2 or i % 5 == 3:
            valores.append(i)
    valores.sort()
    return valores


inicio = int(input())
fim = int(input())

if inicio < fim:
    valores = resto(inicio, fim)
else:
    valores = resto(fim, inicio)
for i in range(len(valores)):
    print(valores[i])
