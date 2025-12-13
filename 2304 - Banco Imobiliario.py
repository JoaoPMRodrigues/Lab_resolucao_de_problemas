i, n = map(int, input().split(" "))
pessoa = {'D': i, 'E': i, 'F': i}
for i in range(n):
    info = list(input().split())
    if info[0] == "C":
        pessoa[info[1]] -= int(info[2])
    elif info[0] == "V":
        pessoa[info[1]] += int(info[2])
    elif info[0] == "A":
        pessoa[info[1]] += int(info[3])
        pessoa[info[2]] -= int(info[3])

print(pessoa['D'], pessoa["E"],pessoa["F"])