def rocks_piles(*data, **conditions):
    first = []

    for ad in data:
        ad = str(ad).lower()
        if (conditions.get('mult_length') is None or len(ad) % conditions.get('mult_length') == 0) \
                and (conditions.get('last_larger') is None or (
        ad[-1] > ad[0] if conditions.get('last_larger') else ad[-1] < ad[0])) \
                and (conditions.get('diff_letters') is None or len(set(ad)) >= conditions.get('diff_letters')) \
                and (conditions.get('presence') is None or ad.find(conditions.get('presence')) != -1):
            first.append(ad)


    return len(min(first, key=len)), ''.join(sorted(set(''.join(first)), reverse=True))


data = ['Alps', 'Putumayo', 'Cordillera', 'Peru']
conditions = {}
print(*rocks_piles(*data, **conditions))

data = ['Talcahuano', 'Alps', 'Putumayo', 'Cordillera', 'Chile', 'Peru']
conditions = {'mult_length': 2, 'last_larger': False, 'diff_letters': 3, 'presence': 'a'}
print(*rocks_piles(*data, **conditions))
