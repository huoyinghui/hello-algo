"""
Semaphore —— 并发上限（模拟下载器）
"""


import threading, time, random

sem = threading.BoundedSemaphore(3)  # 同时最多3个


def download(i: int):
    # with 能确保异常时也会 release
    print(f"[{i}] start\n")
    with sem:
        time.sleep(0.8 + random.random()*0.5)
        print(f"[{i}] done\n")


def main():
    threads = [threading.Thread(target=download, args=(i,)) for i in range(100)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("all downloaded")
    pass


if __name__ == '__main__':
    main()