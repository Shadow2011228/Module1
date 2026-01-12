# Класс - это чертеж для создания готовых продуктов, где:
# готовый продукт - это объект класса.

# В классе есть: атрибуты и методы
# атрибут - это переменная внутри класса вызываемая через . от объекта класса
# метод - это функция внутри класса вызываемая через . от объекта класса

# метод __init__ - это метод который вызывается при создании объекта класса

class Enemy:
    def __init__(self, name, hp, dmg, speed): # def __init__(self) - это конструктор класса
        self.name = name # self.name - это атрибут класса Enemy
        self.hp = hp # - это тоже атрибут класса Enemy
        self.dmg = dmg #- это тоже атрибут класса Enemy
        self.speed = speed

                #self - это аргумент в который кладется переменная объекта класса
    def attack(self): # - это создание метода attack для класса Enemy
        print(f'{self.name} атакует и наносит {self.dmg} урона!')

    def stats(self):
        print(f"{self.name} характиристики:\n"
              f"здоровье {self.hp}\n"
              f"урон {self.dmg}\n"
              f"скорость {self.speed} " )

goblin = Enemy('Гоблин', 10, 1, 50) # Создание объекта(экземпляр) класса
goblin.attack() # Вызов метода attack у объекта класса goblin
goblin.stats()

centaur = Enemy('Кентавр', 100,10,100)# Еще одно создание объекта(экземпляр) класса
centaur.attack()
centaur.stats()

troll = Enemy("Троль", 1000, 100, 10)
troll.attack()
troll.stats()