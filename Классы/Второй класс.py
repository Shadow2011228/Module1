# Создать класс Героя у которого будут:
# имя, здоровье, урон, уровень и опыт
# атака метод атаки, который будет принимать 2 аргумента:
#                                              self и enemy
#       Этот метод будет отнимать от хп врага урок игрока и проверять умер ли враг, враг умер когда его хп достигает 0.
# Когда враг умер должно писать сообщение об этом в консоль

class Hero:
    def __init__(self, name, hp, dmg, levl, exp): # def __init__(self) - это конструктор класса
        self.name = name  # self.name - это атрибут класса Enemy
        self.hp = hp  # - это тоже атрибут класса Enemy
        self.dmg = dmg  # - это тоже атрибут класса Enemy
        self.levl = levl
        self.exp = exp

    def attack(self, enemy): # - это создание метода attack для класса Enemy
        enemy.hp =(enemy.hp- self.dmg)
        print(f'{self.name} атакует {enemy.name} и наносит {self.dmg} dmg по {enemy.name}')

        if enemy.hp <= 0:
            print("Враг убит")
        else:
            print(f'И у него осталось {enemy.hp} хп\n')

    def stats(self):
        print(f"{self.name} характиристики:\n"
              f"здоровье {self.hp}\n"
              f"урон {self.dmg}\n")

class Enemy:
    def __init__(self, name, hp, dmg, speed): # def __init__(self) - это конструктор класса
        self.name = name # self.name - это атрибут класса Enemy
        self.hp = hp # - это тоже атрибут класса Enemy
        self.dmg = dmg #- это тоже атрибут класса Enemy
        self.speed = speed

                #self - это аргумент в который кладется переменная объекта класса
    def attack(self, hero): # - это создание метода attack для класса Enemy
        hero.hp = (hero.hp - self.dmg)
        print(f'{self.name} атакует {hero.name} и наносит {self.dmg} урона!')

        if hero.hp <= 0:
            print("Герой убит")
        else:
            print(f'И у него осталось {hero.hp} хп\n')

    def stats(self):
        print(f"{self.name} характиристики:\n"
              f"здоровье {self.hp}\n"
              f"урон {self.dmg}\n"
              f"скорость {self.speed} " )

goblin = Enemy('Гоблин', 10, 1, 50) # Создание объекта(экземпляр) класса
#goblin.attack(tor) # Вызов метода attack у объекта класса goblin
goblin.stats()

centaur = Enemy('Кентавр', 100,10,100)# Еще одно создание объекта(экземпляр) класса
#centaur.attack(tor)
centaur.stats()

troll = Enemy("Троль", 1000, 100, 10)

tor = Hero("Тор", 1000, 100, 50, 999)

troll.stats()
tor.stats()

for i in range(1,11):
    troll.attack(tor)

    tor.attack(troll)