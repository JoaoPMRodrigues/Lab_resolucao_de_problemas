primeiro = True

while True:
    n = int(input())
    if n == 0:
        break

    if not primeiro:
        print()
    primeiro = False

    turma = []
    
    prioridade = {"P": 1, "M": 2, "G": 3}

    for _ in range(n):
        aluno = {}
        aluno["nome"] = input().strip()
        aluno["cor"], aluno["tamanho"] = input().split()
        turma.append(aluno)

    turma.sort(key=lambda x: (x["cor"], prioridade[x["tamanho"]], x["nome"]))

    for aluno in turma:
        print(aluno["cor"], aluno["tamanho"], aluno["nome"])


