menor_marc = menor_total = nmarc = float("inf")
n = int(input())
for i in range(n):
    soma_ida = list()
    soma_volta = list()
    cnt = 0
    marc = list(map(int, input().split()))
    m = marc[0]
    del (marc[0])
    # subida indo
    soma_ida.append(0)
    for j in range(len(marc)-1):
        if marc[j] < marc[j+1]:
            dif = marc[j+1]-marc[j]
            soma_ida.append(soma_ida[cnt]+dif)
            cnt += 1
    # subida voltando
    soma_volta.append(0)
    cnt = 0
    for j in range(len(marc)-1, 1, -1):
        if marc[j] < marc[j-1]:
            dif = marc[j-1]-marc[j]
            soma_volta.append(soma_volta[cnt]+dif)
            cnt += 1
    # Vendo em qual sentido a trilha tem o menor esforço de subida.
    if soma_ida[-1] <= soma_volta[-1]:
        menor_marc = soma_ida[-1]
        nmarc = m
    else:
        menor_marc = soma_volta[-1]
        nmarc = m
    # Comparando ela com a menor trilha até o momento
    if menor_marc < menor_total:
        menor_total = menor_marc
        nmarc = m
        rsp = i+1
    elif menor_marc == menor_total and m < nmarc:
        nmarc = m
        rsp = i+1
print(rsp)
