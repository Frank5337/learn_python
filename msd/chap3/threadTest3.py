# Email: zbl5337@gmail.com
# Create by Frozen
# Date: 2022/7/21 10:43
import os
import time
import asyncio


async def task(x):
    start = time.time()
    res = 0
    for j in range(98989898):
        res += j
    end = time.time()
    print("Thread:", x, "used: ", end - start, "s result: ", res, "pid:", os.getpid(), ' ppid:', os.getppid())


async def main():
    await asyncio.gather(
        asyncio.create_task(task(1)),
        asyncio.create_task(task(2)),
        asyncio.create_task(task(3))
    )


if __name__ == '__main__':
    t0 = time.time()
    asyncio.run(main())
    t2 = time.time()
    print("Thread:", "main", "used: ", t2 - t0, "pid:", os.getpid(), ' ppid:', os.getppid())
