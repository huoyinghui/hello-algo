"""
生产者 / 消费者
"""

import threading
import time
import random


class Task:
    def __init__(self, ):
        self.condition = threading.Condition()
        self.queue = []


def producer(t: Task = None):
    for i in range(5):
        time.sleep(random.random())
        with t.condition:
            item = f"item-{i}"
            t.queue.append(item)
            print(f"生产: {item}")
            t.condition.notify()  # 通知消费者


def consumer(t: Task = None):
    for _ in range(5):
        with t.condition:
            while not t.queue:
                print(f"消费-wait")
                t.condition.wait()  # 等待有数据
            item = t.queue.pop(0)
            print(f"消费: {item}")


def main():
    task = Task()
    t1 = threading.Thread(target=producer, kwargs=dict(t=task))
    t2 = threading.Thread(target=consumer, kwargs=dict(t=task))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    return


if __name__ == '__main__':
    main()
