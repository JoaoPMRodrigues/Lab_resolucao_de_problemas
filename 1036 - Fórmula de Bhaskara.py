a, b, c = map(float, input().split(" "))
delta = b*b-4*a*c
rdelta = delta**(1/2)

if delta < 0 or a == 0:
    print("Impossivel calcular")
elif delta == 0:
    r = -b/(2*a)
    print(f"R={r}")
else:
    r1 = (-b+rdelta)/(2*a)
    r2 = (-b-rdelta)/(2*a)
    print(f"R1 = {r1:.5f}")
    print(f"R2 = {r2:.5f}")