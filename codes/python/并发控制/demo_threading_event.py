"""
全局停止信号
"""
import threading, time

stop = threading.Event()


def worker(i: int):
    while not stop.is_set():
        print(f"[{i}] working...")
        time.sleep(0.5)
    print(f"[{i}] stopped")


def main():
    threads = [threading.Thread(target=worker, args=(i,)) for i in range(3)]
    for t in threads:
        t.start()
    time.sleep(2)       # 主线程做点别的
    stop.set()          # 广播停止
    for t in threads:
        t.join()
    print("all done")


if __name__ == '__main__':
    main()
