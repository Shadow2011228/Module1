a = \
{
    "ключ": "значение",
    True: 1,
    0: False
}
print(a)
# Добавление элементов
a["Золотой"] = "Золотой ключ"
print(a["Золотой"])
print(a)
# Изменение элементов
a[True] = 2
print(a)
# Достать элементы
pocket = a.pop("Золотой")
print(a)
print(pocket)
# Достать пару ключ-значение
save = a.popitem()
print(a)
print(save)
# Узнать ключи словаря
print(list(a.keys()))
# Узнать значения словаря
print(list(a.values()))
# Очистить словарь
a.clear()
print(a)