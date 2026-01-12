# while - пока
# while условие:
#   действия

"""n = 0
while n < 10:
    print(n)
    n += 1"""

"""s = 0
while True:
    s += int(input("Введите дополнение к сумме: "))
    k = int(input("Введите число(1 - остановка, 2 - продолжение): "))
    if k == 1:
        break
    elif k == 2:
        continue
    else:
        print("Ошибка")
        break

if k == 1:
    print(s)
else:
    print('Ошибка в выполнении программы')"""

"""n = 0
while n < 100:
    if n % 2 == 0:
        continue
    else:
        print(n)
    n+=1"""

def unique(l):
    temp_l = [] # temp - временный
    for i in l:
        if temp_l.count(i) == 0:
            temp_l.append(i)
    return temp_l

h = [1, 1, 2, 3, 4, 4, 4, 4, 5, 5, 6]
print(unique(h))
s_1 = {1, 2, 3, 4, 5, 5}
print(s_1)
print(set(h))
# Множества (set) - набор уникальных(неповторяющихся)элементов