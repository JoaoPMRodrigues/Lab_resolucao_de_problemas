n = int(input())
r = 3
a = 0
for i in range(n):
    a = 1/(6+a)
r += a
print(f"{r:.10f}")