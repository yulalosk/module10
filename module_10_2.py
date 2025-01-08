import threading
import time


class Knight(threading.Thread):
    def __init__(self,name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemy = 100

    def bitva(self, name, power, enemy):
        day = 0
        while enemy != 0:
            time.sleep(1)
            day +=1
            enemy -= power
            print(f'{self.name} сражается {day} дней , осталось {enemy} воинов ')

        print(f'{self.name} одержал победу спустя {day} дней ')



    def run(self):
        print(f'{self.name}, на нас напали!')
        self.bitva(self.name, self.power, self.enemy)



first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print(f'Все битвы закончились ')