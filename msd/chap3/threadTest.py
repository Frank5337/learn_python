# Email: zbl5337@gmail.com
# Create by Frozen
# Date: 2022/7/21 1:32
import os
import time
import threading


def sayhi(x):
    start = time.time()
    res = 0
    for j in range(98989898):
        res += j
    end = time.time()
    print("Thread:", x, "used: ", end - start, "s result: ", res, "pid:", os.getpid())


if __name__ == '__main__':
    start_time = time.time()
    threads = []
    rx = 3
    for i in range(rx):
        thread = threading.Thread(sayhi(i))
        threads.append(thread)

    for i in range(rx):
        threads[i].start()

    for i in range(rx):
        threads[i].join()

    end_time = time.time()
    print("total used ：", end_time - start_time)
