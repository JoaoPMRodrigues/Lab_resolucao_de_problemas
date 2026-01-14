tamanho = 10
X = [1]*tamanho

for i in range(tamanho):
    valor = int(input())
    if valor > 0:
        X[i] = valor

for i in range(tamanho):
    print(f"X[{i}] = {X[i]}")
