"""
#### 1. 数组基础概念
- **定义**：连续内存空间存储相同类型数据的线性数据结构
- **特性**：
  - 随机访问：O(1) 时间复杂度
  - 插入/删除：O(n) 时间复杂度
  - 空间局部性好，缓存友好

#### 2. 静态数组
- **固定大小**：创建后长度不可改变
- **内存分配**：栈或堆上的连续内存
- **应用场景**：已知数据量，查询频繁
"""


class Array(object):

    @classmethod
    def check_index(cls, arr: list, index: int) -> None:
        if index < 0 or index >= len(arr):
            raise Exception("Index out of bounds")
        return
    @classmethod
    def random_access(cls, arr: list, index: int) -> int:
        cls.check_index(arr, index)
        return arr[index]
    

    @classmethod
    def insert(cls, arr: list, index: int, value: int) -> None:
        cls.check_index(arr, index)
        # 把索引 index 以及之后的所有元素向后移动一位
        for i in range(len(arr) - 1, index, -1):
            arr[i] = arr[i - 1]
        # 将 value 赋给 index 处的元素
        arr[index] = value
        return
    
    @classmethod
    def remove(cls, arr: list, index: int) -> None:
        cls.check_index(arr, index)
        last = len(arr) - 1
        for i in range(index, last):
            arr[i] = arr[i + 1]
        # 删除最后一个
        arr.remove(last)
        return
    
    @classmethod
    def traverse(cls, arr: list) -> None:
        # return arr[::-1]
        n = len(arr)
        new_arr = [None] * n
        for i in range(n):
            new_arr[i] = arr[n-1 - i]
        return new_arr
    
    @classmethod
    def find(cls, arr: list, value: int) -> int:
        for i in range(len(arr)):
            if arr[i] == value:
                return i
        return -1
 

def main():
    arr = [1, 2, 3, 4, 5]
    # print(Array.random_access(arr, 2))
    Array.insert(arr, 2, 6)
    #     [1, 2, 6, 3, 4]
    print(arr)
    print(Array.find(arr, 3))
    Array.remove(arr, 2)
    #    [1, 2, 3, 4, 4]
    print(arr)

    print(Array.traverse(arr))



if __name__ == "__main__":
    main()
