import sys

res = []
res1 = ()
p = []
data = list(sys.stdin)

for i in range(len(data)):
    s = str(data[i])
    res = ''
    for j in range(0, len(s), 4):
        res += s[j:j + 3]
    p.append(res.replace('\n', ''))
res1 = set(p)
data = list(res1)
data.sort()
for i in range(len(data)):
    print(data[i])
