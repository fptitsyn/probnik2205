def f(s1, s2, c, m):
    if s1 + s2 <= 30:
        return c % 2 == m % 2
    if c > m:
        return 0
    if s1 % 2 == 0 and s2 % 2 == 0:
        a = [f(s1 - 1, s2, c + 1, m), f(s1, s2 - 1, c + 1, m), f(s1 // 2, s2, c + 1, m), f(s1, s2 // 2, c + 1, m)]
    elif s1 % 2 == 0 and s2 % 2 != 0:
        a = [f(s1 - 1, s2, c + 1, m), f(s1, s2 - 1, c + 1, m), f(s1 // 2, s2, c + 1, m), f(s1, s2 // 2 + 1, c + 1, m)]
    elif s1 % 2 != 0 and s2 % 2 == 0:
        a = [f(s1 - 1, s2, c + 1, m), f(s1, s2 - 1, c + 1, m), f(s1 // 2 + 1, s2, c + 1, m), f(s1, s2 // 2, c + 1, m)]
    else:
        a = [f(s1 - 1, s2, c + 1, m), f(s1, s2 - 1, c + 1, m), f(s1 // 2 + 1, s2, c + 1, m), f(s1, s2 // 2 + 1, c + 1, m)]

    if (c + 1) % 2 == m % 2:
        return any(a)
    else:
        return all(a)

s1 = 18
for s2 in range(13, 100):
    for m in range(1, 7):
        if f(s1, s2, 0, m):
            print(s2, m)
            break
            
