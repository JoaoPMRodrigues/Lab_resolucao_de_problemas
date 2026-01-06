from functools import lru_cache
@lru_cache(None)
def conta_chamadas(posicao):
    if posicao == 0:
        return 0
    elif posicao == 1:
        return 0
    else:
        return conta_chamadas(posicao-1) + conta_chamadas(posicao-2) + 2

@lru_cache(None)
def fibonacci(posicao):
    if posicao == 0:
        return 0
    elif posicao == 1:
        return 1
    else:
        return fibonacci(posicao-1) + fibonacci(posicao-2)


n = int(input())
for _ in range(n):
    pos = int(input())
    print(f"fib({pos}) = {conta_chamadas(pos)} calls = {fibonacci(pos)}")