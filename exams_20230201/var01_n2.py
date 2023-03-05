def scientist(data:str, to_reverse=False):

    global writing
    j = []
    for i in range(len(writing)):
        st = str(writing[i])

        if st > data:
            j.append( ''.join(reversed(st[0::2])) if to_reverse else st[0::2])
        else:
            j.append(''.join(reversed(st[0::3])) if to_reverse else st[0::3])

    writing = tuple(map(str, j))

    return writing
writing = ['yqrweetrstyym', 'fuiopo', 'ezxscvebbhastd', 'slukojihrgeftdsgydma', 'spnogiiusy']
scientist('penetrate', to_reverse=True)
print(writing)


writing = ['lqweeratyrghndseasdx', 'mzxafan', 'sweetyluiiopm']
scientist('wizard')
print(writing)