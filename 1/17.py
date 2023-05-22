f = open("17.txt")

a = [int(i) for i in f]

maxs = 0
c = 0
sr = sum(a) / len(a)
for i in range(1, len(a) - 2):
    if (a[i] * a[i + 1]) > (a[i - 1] * a[i + 2]):
        maxs = max(maxs, a[i] + a[i + 1])
        if a[i] > sr or a[i + 1] > sr:
            c += 1

print(maxs, c)
