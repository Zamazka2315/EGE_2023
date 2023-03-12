sl = input()
bez = sl.split()
o = 0
for i in bez:
    y = len(bez)
    for k in i:
        o += len(k)
print(o)