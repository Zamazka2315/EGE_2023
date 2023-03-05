#
n= int(input())
l = []
for i in range (n):
    l.append(int(input()))
    print(l)
    v = len(l)
    print(l[v - 1])
m = min(l)
print(m)
b = max(l)
print(b)
x = b - m
print(x)