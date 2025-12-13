n = int(input())
for j in range(n):
    # Pegando os valores e a operação
    conta = list(map(str, input().split()))
    n1 = int(conta[0])
    d1 = int(conta[2])
    n2 = int(conta[4])
    d2 = int(conta[6])
    op = conta[3]
    mdc = 0
    # Realizando a operação
    match op:
        case "+":
            n = (n1*d2 + n2*d1)
            d = (d1*d2)
            rsp = f"{n}/{d}"
        case "-":
            n = (n1*d2 - n2*d1)
            d = (d1*d2)
            rsp = f"{n}/{d}"
        case "*":
            n = (n1*n2)
            d = (d1*d2)
            rsp = f"{n}/{d}"
        case "/":
            n = (n1*d2)
            d = (n2*d1)
            rsp = f"{n}/{d}"
    # Verificando o mdc entre o numerador e o denominador
    if n >= d:
        fim = n
    else:
        fim = d
    fim += 1
    for i in range(1, fim):
        if n % i == 0 and d % i == 0 and i > mdc:
            mdc = i
    n /= mdc
    d /= mdc
    rsp1 = f"{n:.0f}/{d:.0f}"
    # print final
    print(f"{rsp} = {rsp1}")
    conta.clear()
