import threading


def f(lock: threading.Lock = None):
    lock.acquire()
    print("第一次拿到锁")
    # 再次获取同一把锁 -> 死锁
    lock.acquire()
    print("不会执行到这里")


def fr(lock: threading.RLock = None):
    lock.acquire()
    print("第一次拿到锁")
    # 再次获取同一把锁 -> 死锁
    lock.acquire()
    print("会执行到这里")


def main():
    lock = threading.RLock()
    fr(lock)
    # lock = threading.Lock()
    # f(lock)


if __name__ == '__main__':
    main()