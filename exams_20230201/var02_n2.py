def parchment(data, divisor=' '):
    data = data.strip()
    global snuffbox
    j = []
    pr = []
    for i in range(len(snuffbox)):
        st = str(snuffbox[i])
        for s in st.strip():
            if s not in data and s not in j:
                j.append(s)
        pr.append(divisor.join(j))
        j = []
    snuffbox = tuple(map(str, pr))

    return snuffbox


snuffbox = ('black', 'powder', 'piece', 'parchment')
parchment('mutabor', divisor=';')
print(snuffbox)

snuffbox = ('black', 'powder', 'piece', 'parchment')
parchment('caliph stork', divisor=' ')
print(snuffbox)
