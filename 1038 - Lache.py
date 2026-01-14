codigo, quantidade = map(int, input().split())
if codigo == 1:
    total = 4*quantidade
elif codigo == 2:
    total = 4.5*quantidade
elif codigo == 3:
    total = 5*quantidade
elif codigo == 4:
    total = 2*quantidade
elif codigo == 5:
    total = 1.5*quantidade

print(f"Total: R$ {total:.2f}")
