# Email: zbl5337@gmail.com
# Create by Frozen
# Date: 2022/7/21 1:59
import os
from threading import Thread
import time


def sayhi(name):
    time.sleep(2)
    print('%s say hello' % name, 'pid:', os.getpid())


if __name__ == '__main__':
    t = Thread(sayhi('egon'))
    t.start()
    print('主线程', 'pid:', os.getpid())
