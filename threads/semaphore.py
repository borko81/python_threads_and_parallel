import threading
import time
import random

semaphore = threading.Semaphore(0)


def consumer():
    # consumer needed semaphore item, becouse of that use semaphore.acquire
    print('Consumer waiting')
    semaphore.acquire()
    print(f'Consumer consume item numer {item}')


def producer():
    global item
    time.sleep(3)
    item = random.randint(1, 100)
    print(f'Producer produce item {item}')
    semaphore.release()


if __name__ == '__main__':
    for i in range(5):
        t1 = threading.Thread(target=producer)
        t2 = threading.Thread(target=consumer)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    print('Program finish')