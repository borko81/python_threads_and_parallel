import threading

shared_resourse = 0
shared_resourse_without_lock = 0
COUNTER = 10000
lock = threading.Lock()


def increament_with_lock():
    global shared_resourse
    for i in range(COUNTER):
        lock.acquire()
        shared_resourse += 1
        lock.release()


def decrement_with_lock():
    global shared_resourse
    for _ in range(COUNTER):
        lock.acquire()
        shared_resourse -= 1
        lock.release()


if __name__ == '__main__':
    t1 = threading.Thread(target=increament_with_lock)
    t2 = threading.Thread(target=increament_with_lock)
    t3 = threading.Thread(target=decrement_with_lock)
    t4 = threading.Thread(target=decrement_with_lock)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()

    print(shared_resourse)
