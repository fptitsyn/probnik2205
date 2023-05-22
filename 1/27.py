f = open("27b.txt")

n = int(f.readline())
a = [int(i) for i in f]

for j in range(0, n):
    for m in range(j + 2, n):
        s = 0
        os = 0
        es = 0
        for i in range(j, m):
            #print(a[i])
            if i % 2 == 0:
                es += a[i]
            else:
                os += a[i]
            s += a[i]

        if os == es:
            print(s)
