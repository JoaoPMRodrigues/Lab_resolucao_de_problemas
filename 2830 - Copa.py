k = int(input())
n = int(input())
lista = [0]*16
for i in range(len(lista)):
    if i == k-1:
        lista[i] = k
    elif i == n-1:
        lista[i] = n
contagem = lista[:]
ctd = 0
aux = []
boole = True
while boole:
    ctd += 1
    for i in range(0, len(contagem)-1, 2):
        if contagem[i] == k and contagem[i+1] == n or contagem[i] == n and contagem[i+1] == k:
            boole = False
            break
        elif contagem[i] == k or contagem[i] == n:
            aux.append(contagem[i])
        elif contagem[i+1] == n or contagem[i+1] == k:
            aux.append(contagem[i+1])
        else:
            aux.append(contagem[i])
    contagem.clear()
    contagem = aux[:]
    aux.clear()
if ctd == 1:
    print("Oitavas")
elif ctd == 2:
    print("quartas")
elif ctd == 3:
    print("semifinal")
else:
    print("final")
