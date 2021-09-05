"""
    Thread with event's
"""

import random
from threading import Thread, Event
import time

items = []
event = Event()


class consumer(Thread):
    def __init__(self, items, event):
        Thread.__init__(self)
        self.items = items
        self.event = event

    def run(self):
        while True:
            time.sleep(2)
            self.event.wait()
            items = self.items.pop()
            print(f"Consumer notify: {items} popped from {self.items}")


class producer(Thread):
    def __init__(self, items, event):
        Thread.__init__(self)
        self.items = items
        self.event = event

    def run(self):
        global item
        for _ in range(5):
            time.sleep(2)
            item = random.randint(0, 257)
            self.items.append(item)
            print(f"Producer notify: item N {item} append to {self.items}")
            self.event.set()
            self.event.clear()


if __name__ == '__main__':
    t1 = producer(items, event)
    t2 = consumer(items, event)
    t1.start()
    t2.start()
    t1.join()
    t2.join()