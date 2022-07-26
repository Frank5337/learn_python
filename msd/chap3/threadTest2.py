# Email: zbl5337@gmail.com
# Create by Frozen
# Date: 2022/7/21 1:32
import os
import time
import asyncio


async def sayhi(x):
    start = time.time()
    res = 0
    for j in range(98989898):
        res += j
    end = time.time()
    print("Thread:", x, "used: ", end - start, "s result: ", res, "pid:", os.getpid())


async def main(loop):
    tasks = []
    for i in range(3):
        print("time begin %s" % i)
        tasks.append(loop.create_task(sayhi(i)))  # 相当于开启了一个线程
        print("sleep time end %s" % i)
        print("*********************")
    await asyncio.wait(tasks)  # 等待所有的任务完成。


if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    loop.close()
    end_time = time.time()
    print("total used ：", end_time - start_time)
