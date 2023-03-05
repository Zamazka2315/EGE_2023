n = int(input())
ls = []

for i in range(n):
    arr = list(map(int, input().split('...')))
    ls.append(arr)
    print(arr)

alrg = input()  # Получить алерген
ms = []

i = 0

for k in range(len(ls)):
    f = ls[k]
    while i < len(f)-1:
        if f[i]<=f[i+1] and str(f[i]).find(alrg) != -1: ms.append(f[i])
        i=i+1
    i=0
    print(sum(ms))
    ms=[]
