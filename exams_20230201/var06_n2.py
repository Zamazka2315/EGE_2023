def consolation(data, add='s'):
    data = data.strip()
    len_dt=len(data)
    global events
    j = ''
    pr = []
    for i in range(len(events)):
        st = str(events[i]).capitalize()
        len_st= len(st) # Длинна строки
        if len_st > len_dt:
            j=(st[:len_dt])
        else:
            j=(st+(len_dt-len_st)*add)
        pr.append(j)
        j = ''
    events = tuple(map(str, pr))

    return events


events = ('veryaui', 'jo', 'to', 'fl')
consolation('bird', add='y')
print(events)

events = ('drum', 'trumpet', 'sanG', 'fluTe')
consolation('stork')
print(events)