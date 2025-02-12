
import heapq
from abc import ABC, abstractmethod

from typing import Any, Callable, List


class Heap(ABC):
    def __init__(self, is_max_heap: bool = False):
        """初始化堆，默认为小顶堆。如果 is_max_heap 为 True，则为大顶堆。
        可以传入一个自定义的比较函数，默认按元素本身进行比较"""
        self.heap = []
        self.is_max_heap = is_max_heap
        # 大顶堆需要取负值
        self.flag = -1 if is_max_heap else 1

    @abstractmethod
    def value(self, v: Any) -> Any:
        """返回堆元素的值，默认直接返回元素本身，或者按照优先级进行转换"""
        if v is None:
            return v
        if isinstance(v, int):
            return self.flag * v
        return v

    def push(self, item: Any) -> None:
        """
        将元素压入堆中（根据堆类型决定顺序）
        """
        heapq.heappush(self.heap, self.value(item))

    def pop(self) -> Any:
        """
        弹出堆顶元素并返回实际值（根据堆类型调整符号）
        """
        v = heapq.heappop(self.heap)
        return self.value(v)

    def peek(self) -> Any:
        """查看堆顶元素（不移除）"""
        return self.value(self.heap[0] if self.heap else None)

    def size(self) -> int:
        """获取堆的大小"""
        return len(self.heap)

    def is_empty(self) -> bool:
        """检查堆是否为空"""
        return not self.heap

    def heapify(self, iterable: List[Any]) -> None:
        """将给定的可迭代对象转化为堆（根据堆类型调整符号）"""
        self.heap = [self.value(item) for item in iterable]
        heapq.heapify(self.heap)
        return


class MinMaxHeap(Heap):
    """
    大堆/小堆
    """
    def value(self, item: Any) -> Any:
        if item is None:
            return None
        return self.flag * item


class Task(object):
    """
    任务类, 优先级和任务类容
    """
    """任务类，包含优先级和任务内容"""

    def __init__(self, priority: int, data: Any):
        self.priority = priority  # 优先级
        self.data = data  # 任务的实际数据

    def __lt__(self, other):
        """根据优先级进行比较，小的优先级优先"""
        return self.priority < other.priority

    def __repr__(self):
        return f"Task(priority={self.priority}, data={self.data})"


class TaskHeap(MinMaxHeap):

    def value(self, item: Task):
        """
        返回任务的优先级
        """
        if item is None:
            return None
        return self.flag * item.priority


class PriorityQueue:
    """优先级队列，基于自定义的 Heap 实现"""
    def __init__(self, is_max_heap=False):
        """初始化队列，默认是小顶堆，is_max_heap 为 True 时使用大顶堆"""
        self.heap = Heap(is_max_heap)

    def push(self, task: Task = None) -> None:
        """将任务按优先级插入队列"""
        self.heap.push(task)
        return

    def pop(self) -> Task:
        """弹出优先级最高的任务"""
        return self.heap.pop()

    def peek(self) -> Task:
        """查看队列中优先级最高的任务"""
        return self.heap.peek()

    def is_empty(self) -> bool:
        """检查队列是否为空"""
        return self.heap.is_empty()

    def size(self) -> int:
        """获取队列大小"""
        return self.heap.size()


def test_max_min_heap():
    # # 创建一个小顶堆
    min_heap = MinMaxHeap(is_max_heap=False)
    # 压入元素
    min_heap.push(5)
    min_heap.push(3)
    min_heap.push(8)
    min_heap.push(1)
    # 获取堆顶元素
    print("Min Heap Peek:", min_heap.peek())  # 1
    # 弹出堆顶元素
    print("Min Heap Pop:", min_heap.pop())  # 1
    print("Min Heap Pop:", min_heap.pop())  # 3

    # 创建一个大顶堆
    max_heap = MinMaxHeap(is_max_heap=True)

    # 压入元素
    max_heap.push(5)
    max_heap.push(3)
    max_heap.push(8)
    max_heap.push(1)

    # 获取堆顶元素
    print("Max Heap Peek:", max_heap.peek())  # 8

    # 弹出堆顶元素
    print("Max Heap Pop:", max_heap.pop())  # 8
    print("Max Heap Pop:", max_heap.pop())  # 5
    # pass
    return


def main():
    # 创建一个优先级队列（小顶堆，优先级低的任务先执行）
    pq = PriorityQueue(is_max_heap=False)

    # 创建任务对象并插入队列
    pq.push(Task(2, "Task 2"))
    pq.push(Task(1, "Task 1"))
    pq.push(Task(3, "Task 3"))

    # 获取队列中的最小优先级任务
    print("Peek:", pq.peek())  # 输出 Task(priority=1, data='Task 1')

    # 弹出任务
    print("Pop:", pq.pop())  # 输出 Task(priority=1, data='Task 1')
    print("Pop:", pq.pop())  # 输出 Task(priority=2, data='Task 2')
    return


if __name__ == '__main__':
    main()
