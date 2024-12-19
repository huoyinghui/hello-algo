from typing import List, Tuple


class HashMapChaining(object):
    """
    基于链式地址实现的哈希表的操作方法发生了以下变化。
    查询元素：输入 key ，经过哈希函数得到桶索引，即可访问链表头节点，然后遍历链表并对比 key 以查找目标键值对。
    添加元素：首先通过哈希函数访问链表头节点，然后将节点（键值对）添加到链表中。
    删除元素：根据哈希函数的结果访问链表头部，接着遍历链表以查找目标节点并将其删除。
    链式地址存在以下局限性。
    占用空间增大：链表包含节点指针，它相比数组更加耗费内存空间。
    查询效率降低：因为需要线性遍历链表来查找对应元素。
    """
    def __init__(self, capacity: int = 4, load: float = 2.0/3.0, extend_ratio: int = 2):
        """

        """
        self.size = 0  # 键值对数量
        self.capacity = capacity  # 哈希表容量
        # 触发扩容的负载因子阈值
        self.load = load
        self.extend_ratio = extend_ratio  # 扩容倍数
        self.buckets = [[] for _ in range(self.capacity)]  # 桶数组

    def hash_func(self, key: int) -> int:
        """哈希函数"""
        return key % self.capacity

    @property
    def load_factor(self) -> float:
        """负载因子"""
        return self.size / self.capacity

    @classmethod
    def _items_link(cls, v_list: List = None):
        """
        v_list: buckets[idx]
        items: 便利某一个bucket中的元素.
        """
        for (key, value) in v_list:
            yield key, value
        return

    @classmethod
    def _items(cls, buckets: List[list] = None):
        """
        items: 字典遍历
        """
        for v_list in buckets:
            if not v_list:
                continue
            for (key, value) in v_list:
                yield key, value
        return

    def items(self):
        """
        items: 字典遍历
        """
        return self._items(self.buckets)

    def extend(self):
        """
        extend

        """
        # 暂存原哈希表
        buckets = self.buckets
        # 初始化扩容后的新哈希表
        self.capacity *= self.extend_ratio
        # 分配新空间
        new_buckets = [[] for _ in range(self.capacity)]
        self.buckets = new_buckets
        self.size = 0
        # 将键值对从原哈希表搬运至新哈希表
        for k, v in self._items(buckets=buckets):
            self.set(k, v)
        return

    def resize(self):
        # 当负载因子超过阈值时，执行扩容
        cur_load = self.load_factor
        if cur_load >= self.load:
            print(f"需要扩容({self.size})  {cur_load} >= {self.load}")
            self.extend()
        return

    def set(self, key, value):
        """
        set
        [
            1: [(key, value), (key, value)],
        ]
        """
        self.resize()
        idx = self.hash_func(key)
        v_list = self.buckets[idx]
        # 检查是否存在
        # 1.存在更新
        for i in range(len(v_list)):
            if v_list[i][0] == key:
                v_list[i][1] = value
                return
        # 不存在-增加
        v_list.append((key, value))
        self.size += 1
        return

    def get(self, key):
        """
        get
        """
        idx = self.hash_func(key)
        v_list = self.buckets[idx]
        for (k, value) in v_list:
            if k == key:
                return value
        return None

    def delete(self, key):
        pass


def main():
    data = HashMapChaining(capacity=3)
    data.set(1, 2)
    data.set(5, 3)
    data.set(11, 3)
    data.set(15, 2)
    # print(data.get(1))
    # print(data.get(11))
    # print(data.get(5))
    # print(data.get(15))

    for k, v in data.items():
        print(f"{k}: {v}")
    pass


if __name__ == '__main__':
    main()
