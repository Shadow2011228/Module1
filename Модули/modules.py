import random

# возвращает рандомное число в перменную
a = random.randint(0, 10)
print(a)

# возврашает рандомный элемент в перменную
shop = ["молоко", "колбаса", "сыр"]
ch = random.choice(shop)
print(ch)

# функция ждет указанное количиство секунд
import time
print(1)
time.sleep(2)
print(2)

# возврашает дату
import datetime

print(datetime.datetime.now().hour)
print(datetime.datetime.now().minute)
print(datetime.datetime.now().second)
print(datetime.datetime.now().year)
print(datetime.datetime.now().month)
print(datetime.datetime.now().day)


import test_module

test_module.test_func1()

import time
print("Отсчет начался ")
time.sleep(int(input("сколько нужно ждать(в секундах):")))
print("Отсчет закончился")
