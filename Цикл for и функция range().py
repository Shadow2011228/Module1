for i in range(10):
    print(i)

print(list(range(30, 0, -1)))
for i in range(30, 0, -1):
    print(f"До взлета осталось, {i}, секунд")
print("Поздравляем вы взлетели!")
#Задание 2
bread = ["Лаваш", "Шаурма", "Буханка", "Чебурек"]
for i in range(len(bread)):
    bread[i] = 1
print(bread)
print(len(bread))
a = ["Лопата", "Топор", "Кирка"]
g = []
for i in range(2, -1, -1):
    g.append(a.pop(0))
print(g)
a = ["Лопата", "Топор", "Кирка"]
a.pop(-1), a.pop(0)
