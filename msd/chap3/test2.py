# Email: zbl5337@gmail.com
# Create by Frozen
# Date: 2022/7/21 2:02
import os
from threading import Thread


class MyThread(Thread):
    def __init__(self, name):
        super(MyThread, self).__init__()
        self.name = name

    # 方法名必须为run
    def run(self):
        print(self.name, 'pid:', os.getpid())


t = MyThread('hugh')
t.start()
print('main', 'pid:', os.getpid())
