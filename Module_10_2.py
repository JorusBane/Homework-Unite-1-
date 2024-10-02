from threading import Thread
from time import sleep

class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemy = 100
        self.time_counter = 0


    def run(self):
        print(f"{self.name}, на нас напали! \n")
        while self.enemy > 0:
            sleep(1)
            self.enemy = self.enemy - self.power
            self.time_counter += 1
            if self.enemy < 0:
                self.enemy = 0
            print(f"{self.name} сражается {self.time_counter} день(дней) ..., осталось {self.enemy} воинов \n")

        print(f"{self.name} одержал победу спустя {self.time_counter} дней(дня)!")
        self.time_counter = 0
        self.enemy = 100


Footman = Knight("Arthas", 20)
Horseman = Knight("Lich King", 40)

Footman.start()
Horseman.start()

Footman.join()
Horseman.join()