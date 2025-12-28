a, b = map(int, input().split())
c = a/b
c1 = a//b
d = b/a
d1 = b//a
if c == c1 or d == d1:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
