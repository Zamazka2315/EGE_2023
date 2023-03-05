def mysteries(data, contrary=False):
    arg = data[::-1] if contrary else data  # Переворачиваем строку если True
    d1 = len(arg)
    global talks
    tt = []
    s = ''
    for i in range(len(talks)):
        lenght = len(talks[i]) if len(talks[i]) < len(arg) else len(arg) #Взять меньшую длинну
        for l in range(lenght):
            s = s + talks[i][l] if talks[i][l] < arg[l] else s + arg[l]
        tt.append(s)
        s = ''
    talks = tuple(map(str, tt))

    return talks

talks = ('wprd', 'zpu', 'fprnotes')
mysteries('upgvoy', contrary=True)
print(talks)

talks = ('reyeal', 'uleis', 'secuezt')
mysteries('thvrrts')
print(talks)
