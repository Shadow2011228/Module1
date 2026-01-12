# Сериализация - это преобразование структуры данных в байты чтобы хранить ее в строке и потом преобразовывать назад

import pickle


dict1 = {'key': 'value', 'key2':'value2'}

bytes = pickle.dumps(dict1) # преобразовали в байты

print(bytes)
print(type(bytes))

dict1 = pickle.loads(bytes) # преобразовали из байтов в словарь
print(dict1)