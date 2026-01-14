n = int(input())
paises = list()
for i in range(n):
    pais = list(map(str, input().split()))
    selecao = dict()
    selecao["nome"] = pais[0]
    selecao["ouro"] = int(pais[1])
    selecao["prata"] = int(pais[2])
    selecao["bronze"] = int(pais[3])
    paises.append(selecao.copy())

paises.sort(key=lambda x: (-x["ouro"], -x["prata"], -x["bronze"], x["nome"]))

for selecao in paises:    
    print(selecao["nome"], selecao["ouro"], selecao["prata"], selecao["bronze"])
