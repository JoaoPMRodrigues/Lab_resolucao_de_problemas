a, b = map(int, input().split())
c = a/b
d = b/a
# Verifica se a é múltiplo de b ou se b é multiplo de a
if c == int(c) or d == int(d):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
