def rivers_names(*data, **conditions):
    first = ''
    second = ''
    result = []
    for ad in data:
        if (conditions.get('difference') is None or abs(len(ad[0]) - len(ad[1])) >= conditions.get('difference')) \
                and (conditions.get('first_presence') is None or str(ad[0]).lower().find(
            conditions.get('first_presence')) != -1) \
                and (conditions.get('common_letter') is None or len(
            set(ad[0].lower()) & set(ad[1].lower())) >= conditions.get('common_letter')) \
                and (conditions.get('second_title') is None or ad[1][0] != conditions.get('second_title')):
            first = first + str(ad[0]).lower()
            second = second + str(ad[1]).lower()
    result.append(''.join(sorted(set(first) - set(second))))
    result.append(''.join(sorted(set(second) - set(first))))

    return result


data = [('Paraguay', 'Uruguay'), ('Tapajos', 'Gapura'), ('Shingu', 'Ucayali'), ('Apure', 'Putumayo')]
conditions = {}

print(*rivers_names(*data, **conditions))

data = [('Amazon', 'Jurua'), ('Parana', 'Madeira'), ('Purus', 'Tocantins'), ('Orinoco', 'Araguaia')]
conditions = {'difference': 1, 'first_presence': 'n', 'common_letter': 2, 'second_title': 's'}
print(*rivers_names(*data, **conditions))
