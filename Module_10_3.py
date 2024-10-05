import random
import threading
import time
from threading import Thread, Lock

lock = threading.Lock()

class Bank:
    def __init__(self):
        self.balance = 0

    def deposit(self):
        for step in range(100):
            random_deposit = random.randint(50, 500)
            self.balance += random_deposit
            time.sleep(0.001)
            print(f"Пополнение на {random_deposit}. Текущий баланс: {self.balance}")
            if self.balance >= 500 and lock.locked():
                lock.release()

    def take(self):
        for step in range(100):
            random_take = random.randint(50, 500)
            print(f"Запрос на {random_take}")
            if random_take <= self.balance:
                self.balance -= random_take
                print(f"Снятие: {random_take}. Баланс: {self.balance}")
            else:
                print("Запрос отклонен, - недостаточно средств")
                lock.acquire()


Tinkoff = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(Tinkoff, ))
th2 = threading.Thread(target=Bank.take, args=(Tinkoff, ))

th1.start()
th2.start()

th1.join()
th2.join()

print(f"Итоговый  баланс {Tinkoff.balance}")