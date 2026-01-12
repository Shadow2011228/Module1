dict1 = {}
print(dict1)

dict2 = {'key1':10, 'key2':2.1, 'key3':True, 'key4':"Hello"}
print(dict2)

dict3 = {1:10,
         2:2.1,
         3:True,
         4:"Hello",
         5:[],
         6:[1, 2, 3]}
print(dict3)

print('= Обращение по ключам =========================')
print(dict2['key1'])
print(dict3[2])


print('= Добавление =========================')
dict2['new key'] = 'new value'
print(dict2)

dict2.update({'new_key2':'new value2'})
print(dict2)

print('= Изменение =========================')
dict2['key1'] = 'new value'
print(dict2)

print('= Удаление и очистка =========================')
del dict2['new key']
print(dict2)

dict2.pop('key1')
print(dict2)

dict2.popitem()
print(dict2)

dict2.clear()
print(dict2)

print('= Вывод =========================')
print(dict3)

print(list(dict3.keys()))

print(list(dict3.values()))

print(list(dict3.items()))
