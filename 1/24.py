a = open("24.txt").readline()
a = a.replace("PR", "*").replace("RP", "*")
a = a.split("*")
print(len(max(a, key=len)))
