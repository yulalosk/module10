import datetime
import threading
import time
from time import thread_time_ns


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding= 'utf-8') as file:
        for w in range(1,word_count+1):
            file.write('Какое-то слово № ' + str(w) + '\n')
            time.sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')

start = datetime.datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end = datetime.datetime.now()
print('Работа потоков', end - start)

start = datetime.datetime.now()
p1 = threading.Thread(write_words(10, 'example5.txt'))
p2 = threading.Thread(write_words(30, 'example6.txt'))
p3 = threading.Thread(write_words(200, 'example7.txt'))
p4 = threading.Thread(write_words(100, 'example8.txt'))
p1.start()
p2.start()
p3.start()
p4.start()
end = datetime.datetime.now()
print('Работа потоков', end - start)