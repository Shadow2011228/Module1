list1 = []
print(list1)

list2 = [10, 2.1, True, "Hello"]
print(list2)

list3 = [10, 2.1, True, "Hello", [], [1,2,3]]
print(list3)

print('=Индексы и срезы=========================')
print(list2[1])
print(list2[1:3])

print('=Добавление=========================')
list1.append('new value')
print(list1)
list1 += ['new value2']
print(list1)

print('=Изменение=========================')
list1[0] = 'new value for index 0'
print(list1)

print('=Удаление и очистка=========================')
del list1[0]
print(list1)

list1.pop(0)
print(list1)

print(list2)
list2.remove("Hello")
print(list2)

list2.pop()
print(list2)

list2.clear()
print(list2)





