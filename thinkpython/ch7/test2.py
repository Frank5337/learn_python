# Email: zbl5337@gmail.com
# Create by Frozen
# Date: 2022/7/2 23:06

import math


def raw_input():
    a = input('请输入:')
    return a


def eval_loop():
    while True:
        line = raw_input()
        if line == 'done':
            print(line)
            break
        print(line, '=', eval(line))


eval_loop()
