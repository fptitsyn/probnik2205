s = "АБ БВ ВГ ГДЕ ДЕ ЕВЗЖ ЗБВ ЖБЗИМ ИАБ ЛАИ МИЛ"
d = {x[0]: x[1:] for x in s.split()}

def f(s, e):
    if s[0] == s[-1] and len(s) > 1:
        return 1
    return sum(f(s + c, e) for c in d[s[-1]] if s.count(c) <= 1)

print(f("И", "И"))
