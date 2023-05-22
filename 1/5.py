def f(n):
    b = bin(n)[2:]
    if n % 2 == 0:
        s = 0
        for i in b:
            s += int(i)
        r = b + str(bin(s)[2:])
    else:
        r = "1" + b + "00"
    return int(r, 2)

ans = []
for i in range(1, 1000):
    r = f(i)
    if r > 215:
        ans.append(i)
        
print(min(ans))
