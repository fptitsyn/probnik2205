from fnmatch import *
for i in range(1, 10**7):
    if fnmatch(str(i), "3*52?"):
        a = set()
        for j in range(1, int(i ** 0.5) + 1):
            if i % j == 0:
                a.add(j)
                a.add(i // j)
        if len(a) % 2 != 0:
            print(i, sorted(a)[-2])
