frequencia = dict()
n = int(input())
for _ in range(n):
    valor = int(input())
    if valor not in frequencia:
        frequencia[valor] = 1
    else:
        frequencia[valor] += 1

for chave, valor in frequencia.items():
    print(f"{chave} aparece {valor} vez(es)")
