def cutting_spot(*data):
    spot = {'2': [], '3': [], '5': []}
    for k in data:

        nmbr = [5, 3, 2]
        for nm in nmbr:
            spot_key = ''
            value = []
            if len(k) % nm == 0:

                if nm == 5:
                    value.append(k.capitalize())
                    spot_key = '5'
                elif nm == 3:
                    value.append(k.lower())
                    spot_key = '3'
                elif nm == 2:
                    value.append(k.swapcase())
                    spot_key = '2'
                else:
                    spot_key = ''

                value.extend(spot.get(spot_key))
                value.sort(reverse=False)
                spot.pop(spot_key)
                spot[spot_key] = value

    return spot


data = [
    'Carpet', 'pILe', 'surface',
    'wOOl', 'graSs', 'Shell', 'armoR'
]
print(cutting_spot(*data))
