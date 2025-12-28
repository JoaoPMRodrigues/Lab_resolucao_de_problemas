lados = list(map(float, input().split()))
lados.sort(reverse=True)
a, b, c = lados[0], lados[1], lados[2]
if a >= b+c:
    print("NAO FORMA TRIANGULO")
else:
    if a**2 == b**2 + c**2:
        print("TRIANGULO RETANGULO")
    elif a**2 > b**2 + c**2:
        print("TRIANGULO OBTUSANGULO")
    else:
        print("TRIANGULO ACUTANGULO")
    if a == b == c:
        print("TRIANGULO EQUILATERO")
    elif (a == b and a != c) or (a == c and a != b) or (b == c and c != a):
        print("TRIANGULO ISOCELES")
