s = input()
dict = {}
j = []
key = []

while len(s) != 0:
    key.append(s.capitalize())
    dict[s.capitalize()] = ''
    s = input()

n = int(input())

v=[]

for i in range(n - 1):
    word = input().lower()
    for k in key:
        for w in word:
            if k.lower().find(w) != -1 and w not in j and w != ' ': j.append(w)
        if len(j) >= 4 and dict[k] == '':  # здесь ошибка в условии
            dict[k] = word
        if len(j) >= 4 and dict[k] != '':
            v = [word,dict[k]]
            v.sort()
            dict[k] = v[0]
            v=[]
        j = []

print(dict)
