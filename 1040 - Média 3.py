n1, n2, n3, n4 = map(float(int, input().split()))

media = (n1*2 + n2*3 + n3*4 + n4)/10
print(f"Media: {media:.1f}")
if media >= 7:
    print("Aluno aprovado.")
elif media < 5:
    print("Aluno reprovado.")
else:
    nr = float(input())
    nova_media = (media+nr)/2
    print("Aluno em exame.")
    print(f"Nota do exame: {nova_media:.1f}")
    if nova_media >= 5:
        print("Aluno aprovado")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {nova_media}")
