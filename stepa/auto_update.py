kolvo = int(input())
k = 0
frazi = []
while k != kolvo:
    frazi.append(input())
    k = k + 1
l = []
k = 0
cis = int(input())
while k != cis:
    l.append(int(input()))
    k = k + 1
for i in l:
    print(frazi[i - 1])