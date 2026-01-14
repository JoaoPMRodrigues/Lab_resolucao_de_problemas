t = int(input())
tot = list()
for i in range(t):
    n = int(input())
    alunos = list(map(str, input().split()))
    freq = list(map(str, input().split()))

    for p in range(len(freq)):
        t = freq[p].count("A")+freq[p].count("P")
        if freq[p].count("P") < 0.75*t:
            tot.append(alunos[p])
    for a in range(len(tot)):
        if a == len(tot)-1:
            print(tot[a], end="")
        else:
            print(tot[a], end=" ")
    print()

    alunos.clear()
    freq.clear()
    tot.clear()
