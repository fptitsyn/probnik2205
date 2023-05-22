from itertools import *
s = "ГОРАДЕТСК"
a = set(["".join(x) for x in set(combinations_with_replacement(s, r=9))])
even = "ОАЕ"
c = 0
for i in a:
    odd_count = 0
    even_count = 0
    for j in i:
        if j in even:
            even_count += 1
        else:
            odd_count += 1
    if "ГД" not in i and "РД" not in i and "ТД" not in i and "СД" not in i:
        if "КД" not in i and "ДГ" not in i and "ДР" not in i:
            if "ДТ" not in i and "ДС" not in i and "ДК" not in i and "ДД" not in i:
                c += 1
            
print(c)
