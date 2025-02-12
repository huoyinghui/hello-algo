
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

    def remove(self, item: Any) -> None:
        """移除指定元素（任务）"""
        try:
            # 这里采用替换删除策略，确保从堆中删除任务
            index = self.heap.index(self.value(item))
            self.heap[index] = self.heap[-1]  # 将最后一个元素移到删除位置
            self.heap.pop()  # 删除最后一个元素
            heapq.heapify(self.heap)  # 重新调整堆
        except ValueError:
            pass  # 如果找不到元素，则跳过


class MinMaxHeap(Heap):
    """
    大堆/小堆
    """
    def value(self, item: Any) -> Any:
        if item is None:
            return None
        return self.flag * item


class PriorityQueue:
    def __init__(self, is_max_heap: bool = False):
        """初始化优先级队列，默认是小顶堆。如果 is_max_heap 为 True，则为大顶堆。"""
        self.is_max_heap = is_max_heap
        self.heap = []
        self.flag = -1 if is_max_heap else 1  # 大顶堆需要取负值，调整优先级顺序

    def push(self, item: Any = None, priority: int = 0):
        """将任务和优先级插入队列"""
        # 插入时将任务的优先级乘以 flag，来实现最大堆或最小堆的功能
        heapq.heappush(self.heap, (self.flag * priority, item))

    def pop(self) -> Any:
        """弹出优先级最高的任务"""
        if not self.is_empty():
            priority, item = heapq.heappop(self.heap)
            return item
        return None

    def peek(self):
        """查看队列中优先级最高的任务，但不弹出"""
        if not self.is_empty():
            priority, item = self.heap[0]
            return item
        return None

    def is_empty(self):
        """检查队列是否为空"""
        return len(self.heap) == 0

    def size(self):
        """返回队列的大小"""
        return len(self.heap)


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


# 测试代码
def test_priority_queue():
    pq = PriorityQueue(is_max_heap=False)  # 小顶堆，优先级低的任务先执行

    pq.push(dict(name='1', data=1), 3)
    pq.push(dict(name='2', data=2), 4)
    pq.push(dict(name='3', data=3), 5)

    print("Peek:", pq.peek())  # 输出 Task 2
    print("Pop:", pq.pop())  # 输出 Task 2
    print("Pop:", pq.pop())  # 输出 Task 3
    print("Pop:", pq.pop())  # 输出 Task 1

    # 使用大顶堆
    pq_max = PriorityQueue(is_max_heap=True)
    pq_max.push("Task A", 1)
    pq_max.push("Task B", 3)
    pq_max.push("Task C", 2)

    print("Peek (max heap):", pq_max.peek())  # 输出 Task B
    print("Pop (max heap):", pq_max.pop())  # 输出 Task B
    print("Pop (max heap):", pq_max.pop())  # 输出 Task C
    print("Pop (max heap):", pq_max.pop())  # 输出 Task A


def main():
    test_priority_queue()
    return


if __name__ == '__main__':
    main()
