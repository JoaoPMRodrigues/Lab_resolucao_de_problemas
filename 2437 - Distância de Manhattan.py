xm, ym, xr, yr = map(int, input().split(" "))
while True:
    if (xm != xr) or (ym != yr):
        n = abs(xm-xr)+abs(ym-yr)
        break
print(n)
