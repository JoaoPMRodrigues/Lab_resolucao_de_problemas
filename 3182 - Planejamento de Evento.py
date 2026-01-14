n, b, h, w = map(int, input().split())
aux = list()
a = list()
p = list()
customin = float("inf")
for i in range(h):
    p.append(int(input()))
    aux = list(map(int, input().split()))
    a.append(aux)

for i in range(h):
    total = int(n*p[i])
    if total < customin:
        customin = total
if customin <= b:
    print(customin)
else:
    print("stay home")