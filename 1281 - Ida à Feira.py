n = int(input())
for i in range(n):
    m = int(input())
    fruta = dict()
    quantidade = list()
    valores = list()
    compras = list()
    for j in range(m):
        fruta["nome"], fruta["preco"] = map(str, input().split())
        fruta["preco"] = float(fruta["preco"])
        valores.append(fruta.copy())
    fruta.clear()
    p = int(input())
    for j in range(p):
        fruta["nome"], fruta["quantidade"] = map(str, input().split())
        fruta["quantidade"] = float(fruta["quantidade"])
        quantidade.append(fruta.copy())
    soma = 0
    for j in range(len(quantidade)):
        for k in range(len(valores)):
            if quantidade[j]["nome"] == valores[k]["nome"]:
                soma += quantidade[j]["quantidade"]*valores[k]["preco"]

    print(f"R$ {soma}")
