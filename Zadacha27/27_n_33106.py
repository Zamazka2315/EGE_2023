# Подъем данных из файла
# Красиво открываем данные
f = open("27_n_33106_B.txt").readlines()

n = int(f[0])  # get N param

f_min = list()
f_max = list()
div = list()

for i in range(1, n + 1):
    num = (list(map(int, f[i].split())))
    f_min.append(min(num))
    f_max.append(max(num))
    div.append(max(num) - min(num))

x = sum(f_min)
div.sort()
print(x)
# При делении на 3 остается либо 2 либо 1 в остатке

if x % 3 == 0:
    print(x)
else:
    for i in div:
        if (x + i) % 3 == 0:
            print(x + i)
            break
