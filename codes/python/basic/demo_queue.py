import queue
import threading
from collections import deque


class QueueBaseMixin(object):
    """
    基础操作
    """
    def _init(self, maxsize):
        self.queue = deque()

    def _qsize(self):
        return len(self.queue)

    def _put(self, item):
        self.queue.append(item)
        return

    def _get(self):
        return self.queue.popleft()


class SafeQueue(QueueBaseMixin):
    """
    参考 queue
    """
    pass

    def __init__(self, maxsize=0):
        self.maxsize = maxsize
        self._init(maxsize)
        # mutex must be held whenever the queue is mutating.  All methods
        # that acquire mutex must release it before returning.  mutex
        # is shared between the three conditions, so acquiring and
        # releasing the conditions also acquires and releases mutex.
        self.mutex = threading.Lock()

        # Notify not_empty whenever an item is added to the queue; a
        # thread waiting to get is notified then.
        self.not_empty = threading.Condition(self.mutex)

        # Notify not_full whenever an item is removed from the queue;
        # a thread waiting to put is notified then.
        self.not_full = threading.Condition(self.mutex)

        # Notify all_tasks_done whenever the number of unfinished tasks
        # drops to zero; thread waiting to join() is notified to resume
        self.all_tasks_done = threading.Condition(self.mutex)
        self.unfinished_tasks = 0

    def qsize(self):
        with self.mutex:
            return self._qsize()

    def empty(self):
        with self.mutex:
            return not self._qsize()


def main():
    q = QueueBaseMixin()
    q._init(5)
    for i in range(5):
        q._put(i)
    ret = q._get()
    print(ret)
    pass


if __name__ == '__main__':
    main()