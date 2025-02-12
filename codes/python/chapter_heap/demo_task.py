import queue


def main():
    # 创建一个优先级队列，默认是小顶堆
    pq = queue.PriorityQueue()

    # 向队列中插入元素，插入时会根据优先级进行排序
    # 优先级低的元素会排在队列的前面
    pq.put((2, 'task 2'))  # 元素格式：(优先级, 任务)
    pq.put((1, 'task 1'))  # 优先级1的任务会优先执行
    pq.put((3, 'task 3'))  # 优先级3的任务会排在后面

    # 获取队列中最小优先级（即最先执行的任务）
    item = pq.get()  # 弹出优先级最小的元素
    print(item)  # 输出 (1, 'task 1')

    item = pq.get()  # 下一个最小优先级的任务
    print(item)  # 输出 (2, 'task 2')

    # 查看队列是否为空
    print("Queue empty:", pq.empty())  # False

    # 获取队列大小
    print("Queue size:", pq.qsize())  # 1


if __name__ == '__main__':
    main()