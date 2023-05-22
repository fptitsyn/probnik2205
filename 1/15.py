def d(n, m):
    return n % m == 0

for a in range(1, 1000):
    for x in range(1, 1000):
        if not((d(x, 12) <= (not d(x, 90))) or ((x + 2 * a) >= 512)):
            break
    else:
        print(a)
        break

