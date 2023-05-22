from functools import lru_cache
from sys import setrecursionlimit
setrecursionlimit(1000000)
@lru_cache()
def f(n):
    if n < 2:
        return 1
    if n % 3 == 0:
        return f(n // 3) - 1
    return f(n - 1) + 17

c = 0
for n in range(1, 100000 + 1):
    r = f(n)
    if r == 43:
        c += 1

print(c)
