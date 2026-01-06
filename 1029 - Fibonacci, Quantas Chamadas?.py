num_chamadas = -1


def fibonacci(posicao):
    global num_chamadas
    if posicao == 0:
        num_chamadas += 1
        return 0
    elif posicao == 1:
        num_chamadas += 1
        return 1
    else:
        num_chamadas += 1
        return fibonacci(posicao-1) + fibonacci(posicao-2)


n = int(input())
for _ in range(n):
    pos = int(input())
    print(f"fib({pos}) = {fibonacci(pos)} calls = {num_chamadas}")
    num_chamadas = 1
