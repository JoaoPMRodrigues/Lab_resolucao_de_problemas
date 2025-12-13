n = float(input())
# Notas
n100 = n//100
r = n % 100
n50 = r//50
r = r % 50
n20 = r//20
r = r % 20
n10 = r//10
r = r % 10
n5 = r//5
r = r % 5
n2 = r//2
r = r % 2
# Moedas
r *= 100
m1 = r//100
r = r % 100
m50 = r//50
r = r % 50
m25 = r//25
r = r % 25
m10 = r//10
r = r % 10
m5 = r//5
r = r % 5
m01 = r//1
print("NOTAS:")
print(f"{n100:.0f} nota(s) de R$ 100.00")
print(f"{n50:.0f} nota(s) de R$ 50.00")
print(f"{n20:.0f} nota(s) de R$ 20.00")
print(f"{n10:.0f} nota(s) de R$ 10.00")
print(f"{n5:.0f} nota(s) de R$ 5.00")
print(f"{n2:.0f} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{m1:.0f} moeda(s) de R$ 1.00")
print(f"{m50:.0f} moeda(s) de R$ 0.50")
print(f"{m25:.0f} moeda(s) de R$ 0.25")
print(f"{m10:.0f} moeda(s) de R$ 0.10")
print(f"{m5:.0f} moeda(s) de R$ 0.05")
print(f"{m01:.0f} moeda(s) de R$ 0.01")
