import random
import threading
import time

lock = threading.Lock()
counter = 0


def task():
    global counter
    time.sleep(random.random() * 0.001)
    for _ in range(10000):
        with lock:
            counter += 1


def main():
    threads = [threading.Thread(target=task) for _ in range(100)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(counter)
    return


if __name__ == '__main__':
    main()
