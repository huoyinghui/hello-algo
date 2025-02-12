
import heapq

from typing import List


class Heap(object):
    def __init__(self, is_max_heap: bool = False):
        """初始化堆，默认为小顶堆。如果 is_max_heap 为 True，则为大顶堆。"""
        self.heap = []
        self.is_max_heap = is_max_heap
        # 大顶堆需要取负值
        self.flag = -1 if is_max_heap else 1

    def value(self, v: int | None = 0):
        """
        flag * v
        """
        if v is None:
            return None
        return self.flag * v

    def push(self, item: int = 0):
        """
        将元素压入堆中（根据堆类型决定顺序）
        """
        heapq.heappush(self.heap, self.value(item))
        return

    def pop(self):
        """
        弹出堆顶元素并返回实际值（根据堆类型调整符号）。
        """
        v = heapq.heappop(self.heap)
        return self.value(v)

    def peek(self):
        """
        查看堆顶元素（不移除）。
        """
        return self.value(self.heap[0] if self.heap else None)

    def size(self) -> int:
        """获取堆的大小。"""
        return len(self.heap)

    def is_empty(self) -> bool:
        """检查堆是否为空。"""
        return not self.heap

    def heapify(self, iterable: List[int]) -> None:
        """将给定的可迭代对象转化为堆（根据堆类型调整符号）。"""
        self.heap = [self.value(item) for item in iterable]
        heapq.heapify(self.heap)
        return


def main():
    # 创建一个小顶堆
    # min_heap = Heap(is_max_heap=False)
    # # 压入元素
    # min_heap.push(5)
    # min_heap.push(3)
    # min_heap.push(8)
    # min_heap.push(1)
    # # 获取堆顶元素
    # print("Min Heap Peek:", min_heap.peek())  # 1
    # # 弹出堆顶元素
    # print("Min Heap Pop:", min_heap.pop())  # 1
    # print("Min Heap Pop:", min_heap.pop())  # 3

    # 创建一个大顶堆
    max_heap = Heap(is_max_heap=True)

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
    pass
    return


if __name__ == '__main__':
    main()
