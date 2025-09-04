import threading

lock = threading.Lock()
counter = 0


def task():
    global counter
    for _ in range(100000):
        # with lock:  # 等价于 lock.acquire() / lock.release()
        #     counter += 1
        # lock.acquire()
        counter += 1
        # lock.release()


def main():
    threads = [threading.Thread(target=task) for _ in range(5)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(counter)
    return


if __name__ == '__main__':
    main()
