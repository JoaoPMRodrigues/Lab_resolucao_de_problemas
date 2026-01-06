memoria_posicao = {}
memoria_chamada = {}


def conta_chamadas(posicao):
    if posicao in memoria_posicao:
        return memoria_posicao[posicao]
    elif posicao <= 1:
        resultado = 0
    else:
        resultado = conta_chamadas(posicao-1) + conta_chamadas(posicao-2) + 2
    memoria_posicao[posicao] = resultado
    return resultado


def fibonacci(posicao):
    if posicao in memoria_chamada:
        return memoria_chamada[posicao]
    elif posicao <= 1:
        resultado = posicao
    else:
        resultado = fibonacci(posicao-1) + fibonacci(posicao-2)
    memoria_chamada[posicao] = resultado
    return resultado


n = int(input())
for _ in range(n):
    pos = int(input())
    print(f"fib({pos}) = {conta_chamadas(pos)} calls = {fibonacci(pos)}")
