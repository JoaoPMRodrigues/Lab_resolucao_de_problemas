n = int(input())
for i in range(n):
    n, m = map(int, input().split())
    renas = list()
    for j in range(n):
        rena = dict()
        rena["nome"], rena["peso"], rena["idade"], rena["altura"] = map(str, input().split())
        rena["peso"], rena["idade"], rena["altura"] = int(rena["peso"]), int(rena["idade"]), float(rena["altura"])
        renas.append(rena.copy())
    renas.sort(key=lambda x: (-x["peso"], x["idade"], x["altura"],x["nome"]))
    print("CENARIO {"+f"{i+1}"+"}")
    for j in range(m):
        print(f"{j+1} - {renas[j]['nome']}")