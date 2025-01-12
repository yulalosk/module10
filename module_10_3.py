import threading
from random import randint
import time

class Bank(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.balance = 500
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            sum_ = randint(50, 500)
            with self.lock:
                if self.balance >= 500 and not self.lock.locked():
                    self.lock.release()
            self.balance += sum_
            print(f'Пополнение: {sum_}. Баланс: {self.balance}')
        time.sleep(0.001)


    def take(self):
        for i in range(100):
            sum_ = randint(50, 500)
            print('Запрос на снятие', sum_)
            with self.lock:
                if sum_ <= self.balance:
                    self.balance -= sum_
                    print(f'Снятие: {sum_}. Баланс: {self.balance}')
                    time.sleep(0.001)

                else:
                    print(f'запрос отклонен, недостаточно средств')
                    self.lock.acquire()
            time.sleep(0.001)


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')