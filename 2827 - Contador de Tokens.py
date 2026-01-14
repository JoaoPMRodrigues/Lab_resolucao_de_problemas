p = list(map(str, input().lower().split()))
cnt = []
maior=-float("inf")
ac=[]
for i in range(len(p)):
    for j in range(len(p[i])-1):
        plv = p[i][j]+p[i][j+1]
        cnt.append(plv)

freq = {}
for par in cnt:
    freq[par] = freq.get(par, 0) + 1

for par, qnt in freq.items():
    if qnt > maior:
        maior = qnt
        maiort = par
    elif qnt==maior:
        if maiort[0]>par[0]:
            maior = qnt
            maiort = par
print(f"{maiort}:{maior}")