while True:
    try:
        vogais=str(input())
        frase=str(input())
        principal=[]
        soma=[]
        soma.append(0)
        c=0
        for v in vogais:
            principal.append(frase.count(v))
            soma.append(principal[c]+soma[c])
            c+=1
        print(soma[-1])
    except EOFError:
        break 