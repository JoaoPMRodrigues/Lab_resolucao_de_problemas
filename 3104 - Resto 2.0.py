import sys
A = sys.stdin.readline().strip()
B = int(sys.stdin.readline().strip())
resto = 0
for d in A:
    resto = (resto * 10 + int(d)) % B
print(resto)
