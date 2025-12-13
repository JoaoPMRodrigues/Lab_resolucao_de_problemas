n = int(input())
presentes = list()
lista = list()
total_boas = total_mas = 0
for i in range(n):
    crianca = dict()
    crianca["boa"], crianca["nome"] = map(str, input().split())
    lista.append(crianca.copy())
    if crianca["boa"] == "+":
        total_boas += 1
    else:
        total_mas += 1
lista.sort(key=lambda x: x["nome"])
for crianca in lista:
    print(crianca["nome"])
print(f"Se comportaram: {total_boas} | Nao se comportaram: {total_mas}")