import heapq
import itertools
from dataclasses import dataclass, field
from typing import Any


def heapsort(iterable):
    """
    堆排序
    """
    n = []
    for v in iterable:
        heapq.heappush(n, v)
    items = [heapq.heappop(n) for i in range(len(n))]
    return items


@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any = field(compare=False)


class QueueSrv:
    def __init__(self):
        self.items = []
        self.pq = []  # list of entries arranged in a heap
        self.entry_finder = {}  # mapping of tasks to entries
        self.REMOVED = '<removed-task>'  # placeholder for a removed task
        self.counter = itertools.count()  # unique sequence count

    def add_task(self, task, priority=0):
        'Add a new task or update the priority of an existing task'
        if task in self.entry_finder:
            self.remove_task(task)
        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heapq.heappush(self.pq, entry)

    def remove_task(self, task):
        """
        remove
        """
        entry = self.entry_finder.pop(task)
        entry[-1] = self.REMOVED

    def pop_task(self):
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        while self.pq:
            priority, count, task = heapq.heappop(self.pq)
            if task is not self.REMOVED:
                del self.entry_finder[task]
                return task
        raise KeyError('pop from an empty priority queue')


def main():
    # n = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
    # print(n)

    from collections import deque
    nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]

    task = deque(nums, maxlen=3)
    print(task)
    pass


if __name__ == '__main__':
    main()


