def f(x, q):
    x = x[::-1]
    a = 0
    for i in range(len(x)):
        a += x[i] * q ** i
    return(a)


for x in range(15):
    for y in range(17):
        a1 = f([1, 2, 3, x, 5], 15)
        a2 = f([6, 7, y, 7], 17)
        d = a1 + a2
        if d % 131 == 0:
            print(x, y, d // 131)
