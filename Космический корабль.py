import time

eat = int(input("Сколько еды потребуется?:"))
oxygen=int(input("Сколько кислорода потребуется?:"))

for i in range(eat):
    time.sleep(1)
    eat -= 1
    print(f"осталось {eat} еды")

for i in range(oxygen):
    time.sleep(1)
    oxygen -= 1
    print(f"осталось {oxygen} кислорода")