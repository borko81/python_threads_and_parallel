from threading import Thread
import threading
from time import sleep


def fib_calc(begin, end):
    """ Calculae fib """
    a, b = 0, begin

    while b < end:
        print(b)
        a, b = b, a + b


class CookBook(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.message = "This is my thread"

    def print_message(self):
        print(self.message)

    def run(self):
        print("Threadind start\n")
        x = 0
        while x < 10:
            self.print_message()
            sleep(1)
            x += 2
        print("Thread end\n")


def function_i(i):
    name = threading.current_thread().getName()
    print(f" {name} function {i}")
    return


if __name__ == '__main__':
    threads = []
    for i in range(10):
        t = threading.Thread(target=function_i, args=(i,))
        threads.append(t)
        t.start()
        t.join()
