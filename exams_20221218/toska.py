n = int(input())  # get N param

grst = []
rdst = []

for i in range(1, n + 1):
    num = input()

    if int(num) % 7 == 0 and num not in grst and int(num) % 2 != 0: grst.append(num)
    if int(num) % 4 == 0 and num not in rdst: rdst.append(num)

print(f'Тоска ... ', '.'.join(grst))
print(f'Радость!', '!'.join(rdst))


while i<7:
    print(i)

