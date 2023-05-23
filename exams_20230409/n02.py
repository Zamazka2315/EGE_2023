data = [
    'graCeful Trout', 'silver Perch',
    'hUge Salmon melangE', 'fast Pike',
    'Trout huge', 'strong Pike',
    'Pike predatory'
]


def angling(*data):
    fish = {}
    for k in data:
        fish_key = ""
        value = []
        for st in k.split():

            if st.istitle():
                fish_key = st
            else:
                value.append(st.lower())
        if fish_key not in fish.keys():
            value.sort(reverse=True)
            fish[fish_key] = value
        else:

            value.extend(fish.get(fish_key))
            value.sort(reverse=True)
            print(value)
            fish.pop(fish_key)
            fish[fish_key] = value

    return fish


print(angling(*data))
