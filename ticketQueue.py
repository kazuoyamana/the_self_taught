import time
import random


class Queue:
    """First in First Out Queueing system"""
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def simulate_line(till_show, max_time):
    """To simulate the time for people waiting to buy a ticket"""
    pq = Queue()
    tix_sold = []

    for i in range(100):
        pq.enqueue("person" + str(i))

    t_end = time.time() + till_show
    now = time.time()

    while now < t_end and not pq.is_empty():
        now = time.time()
        r = random.randint(0, max_time)
        time.sleep(r)
        person = pq.dequeue()
        print(person)
        tix_sold.append(person)

    return tix_sold


# 上映まで30秒、最大5秒かかるとして何人に売ることができるか計測
sold = simulate_line(30, 5)
print(sold)
