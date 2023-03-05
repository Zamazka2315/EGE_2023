s = input()
ls = []
r = 0
count = 0
a = []

while s != '':
    arr = list(map(int, s.split('-')))
    for n in arr:
        if n % 10 == 1 and n != 0:
            count = count + 1
            a.append(str(n))
    if count > r:
        r = count
        ls = a
    count = 0
    a = []
    s = input()

print(' '.join(ls))
