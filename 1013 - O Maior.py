a = list(map(int, input().split()))
for i in range(len(a)):
    for j in range(i, len(a)):
        if a[i] < a[j]:
            a[i], a[j] = a[j], a[i]
print(f"{a[0]} eh o maior")
