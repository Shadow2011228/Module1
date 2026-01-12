tuple1 = ()
print(tuple1)

tuple2 = (10, 2.1, True, "Hello")
print(tuple2)

tuple3 = (10, 2.1, True, "Hello", [], [1, 2, 3])
print(tuple3)

print('=Индексы и срезы=========================')
print(tuple2[1])
print(tuple2[1:3])

print('=Уничтожение переменно=========================')
del tuple1
print(tuple1)
