s = input()
dict = {}
j = []
key = []

while len(s) != 0:
    key.append(s.lower())
    dict[s] = ''
    s = input()

n = int(input())

for i in range(n - 1):
    word = input().lower()
    for k in key:
        for w in word:
            if k.find(w) != -1 and w not in j and w != ' ': j.append(w)
        if len(j) >= 5 and dict[k] == '':  # здесь ошибка в условии
            dict[k] = word
        j = []

for key, value in dict.items():
    if value == '':
        del dict[key]

print(dict)
