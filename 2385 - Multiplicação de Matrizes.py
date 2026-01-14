N = int(input())
P, Q, R, S, X, Y = map(int, input().split())
I, J = map(int, input().split())
soma = 0
for k in range(1, N + 1):
    Aik = (P * I + Q * k) % X
    Bkj = (R * k + S * J) % Y
    soma += Aik * Bkj
print(soma)