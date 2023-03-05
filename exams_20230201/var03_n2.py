def birds_talking(data, great=False):
    d1 = len(data)
    global stork_chat
    for i in range(len(stork_chat)):

        s = stork_chat[i].strip()
        stork_chat[i] = s[::-d1].upper() if great else s[::-d1].lower()

    return stork_chat


stork_chat = ['skpkoiruyotrtwqS', 'savi', 'SklyhmanbwvclxZa', 'tgtrnewiqakasldfaght', 'itiuuytorebqwa',
              'gjhngfidshaqtweertmyuoopS']
birds_talking('tor', great=True)
print(stork_chat)

stork_chat = ['terseewhqT', 'ieurYa', 'yarpeov', 'hygnfndusf', 'svdcrxizB']
birds_talking('OK')
print(stork_chat)
