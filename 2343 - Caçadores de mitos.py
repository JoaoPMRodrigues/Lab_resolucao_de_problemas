
#Variáveis
lista = list()
boole = False
vistos=set()

n = int(input())
# Onde cada raio caiu
for i in range(n):
    lista.append(input().split())
#Verificando se cairam 2 no mesmo lugar
for par in lista:
    tupla = (int(par[0]), int(par[1]))
    if tupla in vistos:
        boole = True
        break
    vistos.add(tupla)
print(vistos)
#Se caiu, print 1, senão print 0
if boole:
    print(1)
else:
    print(0)
