# Email: zbl5337@gmail.com
# Create by Frozen
# Date: 2022/7/21 14:52
# success
import os
from threading import Thread
import time
NUM_THREADS = 3


def sayhi(x):
    start = time.time()
    res = 0
    for j in range(98989898):
        res += j
    end = time.time()
    print("Thread:", x, "used: ", end - start, "s result: ", res, "pid:", os.getpid(), "\n")


if __name__ == '__main__':
    start_time = time.time()
    threads = []
    for j in range(NUM_THREADS):
        thread = Thread(target=sayhi, args=(j,))
        threads.append(thread)
    for i in range(NUM_THREADS):
        threads[i].start()

    for i in range(NUM_THREADS):
        threads[i].join()

    end_time = time.time()
    print("total used ：", end_time - start_time)


# class MyThread(Thread):
#     def __init__(self, name='Python3'):
#         super().__init__()
#         self.name = name
#
#     def run(self):
#         start = time.time()
#         res = 0
#         for j in range(98989898):
#             res += j
#         end = time.time()
#         print("Thread:", self.name, "used: ", end - start, "s result: ", res, "pid:", os.getpid())

# if __name__ == '__main__':
#     start_time = time.time()
#     sayhi(9)
#     end_time = time.time()
#     print("total used ：", end_time - start_time)