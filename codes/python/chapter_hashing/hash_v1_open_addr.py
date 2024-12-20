import abc
from typing import List, Tuple


class Hash:
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

    @abc.abstractmethod
    def put(self, key: str | int = None):
        pass

    @abc.abstractmethod
    def get(self, key: str | int = None):
        pass

    @classmethod
    def items(cls, buckets: List[list] = None):
        """
        items: 字典遍历
        """
        for v in buckets:
            if not v:
                continue
            yield v
        return

    def print(self):
        for key, v in self.items(buckets=self.buckets):
            print(key, v)


class HashOpenAddrV1(Hash):
    """
    开放寻址

    线性探测:
        插入元素：通过哈希函数计算桶索引，若发现桶内已有元素，则从冲突位置向后线性遍历（步长通常为1），
            直至找到空桶，将元素插入其中。
        查找元素：若发现哈希冲突，则使用相同步长向后进行线性遍历，直到找到对应元素，返回 value 即可；
            如果遇到空桶，说明目标元素不在哈希表中，返回 None 。
    """

    def __init__(self, capacity: int = 4, load: float = 2.0 / 3.0, extend_ratio: int = 2):
        """
        """
        super().__init__(capacity, load, extend_ratio)
        self.buckets: List = [None] * self.capacity  # 桶数组

    def is_ok(self, key: str | int = '', i: int = 0, cnt: int = 0) -> Tuple[bool, int]:
        if not self.buckets[i]:
            return True, cnt
        # 有
        if self.buckets[i][0] == key:
            return True, cnt
        cnt += 1
        print(f"key {key} 冲突次数 {cnt}")
        return False, cnt

    def is_ok_get(self, key: str | int = '', i: int = 0, cnt: int = 0) -> Tuple[bool, int]:
        # 当前key对应的hash 没有存储过
        if not self.buckets[i]:
            # 此时，字典不存在key
            return True, cnt
        # 有 key hash: 可能有一组
        if self.buckets[i][0] == key:
            return True, cnt
        cnt += 1
        print(f"key {key} 冲突次数 {cnt}")
        return False, cnt

    def find_idx(self, key: str | int = '') -> int:
        """
        搜索 key 对应的桶索引
        """
        index = self.hash_func(key)
        # bucket[index, size]
        cnt = 0
        for i in range(index, self.capacity):
            ok, cnt = self.is_ok(key, i, cnt)
            if ok:
                return i
        # bucket[0, index]
        for i in range(0, index):
            ok, cnt = self.is_ok(key, i, cnt)
            if ok:
                return i
        raise ValueError(f"not find empty idx {key}")

    def find_idx_get(self, key: str | int = '') -> int:
        """
        搜索 key 对应的桶索引
        """
        index = self.hash_func(key)
        cnt = 0
        for i in range(index, self.capacity):
            ok, cnt = self.is_ok_get(key, i, cnt)
            if ok:
                return i
        # bucket[0, index]
        for i in range(0, index):
            ok, cnt = self.is_ok_get(key, i, cnt)
            if ok:
                return i
        return None

    def put(self, key: str | int = '', v=None):
        idx = self.find_idx(key)
        self.buckets[idx] = (key, v)
        return

    def get(self, key: str | int = None, default=None):
        idx = self.find_idx_get(key)
        if not idx:
            return default
        v = self.buckets[idx]
        if not v:
            return None
        return v[0]


def main():
    # 初始化哈希表
    hashmap = HashOpenAddrV1(capacity=100)

    # 添加操作
    # 在哈希表中添加键值对 (key, val)
    hashmap.put(200, "A")
    hashmap.put(500, "D")
    hashmap.put(300, "Y")
    hashmap.put(76, "小法")
    hashmap.put(876, "小鸭")
    print("\n添加完成后，哈希表为\nKey -> Value")
    hashmap.print()

    # 查询操作
    # 向哈希表中输入键 key ，得到值 val
    name = hashmap.get(13276, '')
    print("\n输入学号 13276 ，查询到姓名 " + name)

    # 删除操作
    # 在哈希表中删除键值对 (key, val)
    # hashmap.remove(16750)
    # print("\n删除 16750 后，哈希表为\nKey -> Value")
    hashmap.print()
    pass


if __name__ == "__main__":
    main()