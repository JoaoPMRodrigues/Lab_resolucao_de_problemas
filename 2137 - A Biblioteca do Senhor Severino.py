while True:
    try:
        n = int(input())
        livros = list()
        for i in range(n):
            livros.append(str(input()))
        livros.sort()
        for i in range(len(livros)):
            print(livros[i])
    except EOFError:
        break