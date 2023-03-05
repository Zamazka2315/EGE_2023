s = ''
m = 0
e = 0
t = 0

while s.find("Morning") == -1:
    if s.find('monst') != -1 and s.find('evil') != -1:
        t = t + 1
    elif s.find('monst') != -1:
        m = m + 1
    elif s.find('evil') != -1:
        e = e + 1
    s = input()

print(m, e, t)
