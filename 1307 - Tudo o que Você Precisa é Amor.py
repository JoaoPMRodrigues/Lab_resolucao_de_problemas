import math
n = int(input())
for i in range(1, n+1):
    #recebendo o valor e transformando em binário
    n1 = int(input(), 2)
    n2 = int(input(), 2)
    #mdc de n1 e n2
    g = math.gcd(n1, n2)
    if g > 1:
        print(f"Pair #{i}: All you need is love!")
    else:
        print(f"Pair #{i}: Love is not all you need!")
