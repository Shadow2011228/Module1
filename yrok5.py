a = ["Кирка", "Факела", "Еда"]
a[0]= "Железная кирка"
print(a)
del a[1]
print(a)
a.append(23.5)
print(a)
a = a[:1] + ["Меч"] + a[1:]
print(a)
pocket = a.pop(0)
print(a)
print(pocket)
i = int(input("Введите номер элемента, который хотите сделать топором "))
a[i-1] = "Топор"
print(a)