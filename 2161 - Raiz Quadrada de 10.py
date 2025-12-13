n = int(input())
r = 3
a = 0
for i in range(n):
    if n == 0:
        a = 0
        break
    else:
        a = 1/(6+a)
r += a
print(f"{r:.10f}")
