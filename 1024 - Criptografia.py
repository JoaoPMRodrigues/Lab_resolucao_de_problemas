n=int(input())
tabela=":;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_´abcdefghijklmnopqrstuvwxyz{|}-"
for i in range(n):
    palavra = str(input())
    print(palavra)
    for letra in palavra:
        if letra.isalpha():
            posicao = tabela.index(letra)
            codigo=""
            if (posicao+3)>(len(tabela)-1):
                codigo+= tabela[posicao+3-26]
            else:
                codigo += tabela[posicao+3]
        else:
            codigo += letra
    inverso  = ""
    for i in range(len(codigo)-1,-1,-1):
        inverso += codigo[i]
    inicio = len(inverso)//2
    for i in range(inicio,len(inverso)):
        if inverso[i].isalpha():
            posicao = tabela.index(letra)
            codigo=""
            if (posicao+3)>(len(tabela)-1):
                codigo+= tabela[posicao+3-26]
            else:
                codigo += tabela[posicao+3]
        else:
            codigo += letra
    print(codigo)