frequencia = dict()
valores = list()
n = int(input())
for _ in range(n):
    valor = int(input())
    valores.append(valor)

valores.sort()
for i in range(len(valores)):
    if valores[i] not in frequencia:
        frequencia[valores[i]] = 1
    else:
        frequencia[valores[i]] += 1

for chave, valor in frequencia.items():
    print(f"{chave} aparece {valor} vez(es)")