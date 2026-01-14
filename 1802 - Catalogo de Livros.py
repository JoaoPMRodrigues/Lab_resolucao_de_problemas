listas = []
for _ in range(5):
    linha = list(map(int, input().split()))
    q = linha[0]
    valores = linha[1:]
    listas.append(valores)

K = int(input())

# Geramos TODAS as combinações possíveis

combinacoes = []
for port in listas[0]:
    for mat in listas[1]:
        for fis in listas[2]:
            for quim in listas[3]:
                for bio in listas[4]:
                    combinacoes.append(port + mat + fis + quim + bio)

# Ordenar do maior para o menor

combinacoes.sort(reverse=True)

# Somar os K maiores

soma = 0
for i in range(K):
    soma += combinacoes[i]
print(soma)
