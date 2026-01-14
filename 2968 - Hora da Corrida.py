v, n = map(int, input().split())
t = n*v
for i in range(10, 100, 10):
    r = t * i / 100
    if r == int(r):
        r = int(r)
    else:
        r = int(r) + 1
    if i == 90:
        print(f"{r}")
    else:
        print(f"{r}", end=" ")
