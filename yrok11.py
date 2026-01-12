def math_sum(l):
    h=0
    for i in l:
        if type(i) ==  int or type(i) == float and type(i) % 2 == 0:
            h+=i
    return h
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "Слон"]
print(math_sum(a))

def unque(str_1):
    temp_dict = {}
    for i in range(len(str_1)):
        if str_1[i] != " ":
            if str_1[i] in list(temp_dict.keys()):
                temp_dict[str_1[i]] += 1
            else:
                temp_dict[str_1[i]] = 1
    return temp_dict
s = "Мороз и солнце день чудесный"
print(unque(s))