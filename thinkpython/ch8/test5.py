# Email: zbl5337@gmail.com
# Create by Frozen
# Date: 2022/7/3 23:36


def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
    return False


print(any_lowercase1('ABC'))


def any_lowercase2(s):
    for c in s:
        if c.islower():
            return 'True'
    return 'False'


print(any_lowercase2('AbC'))


def any_lowercase3(s):
    flag = False
    for c in s:
        flag = c.islower()
        if flag:
            return True
    return flag


print(any_lowercase3('AbC'))

# 说明
# 1、or逻辑或，一真则真，都假才假，可以对符号两侧的值进行或运算。
#
# 2、或运算两个值中只要有一个True，就会返回True。
#
# Python中的或运算是短路的或， 或运算是找True的， 如果第一个值为True，则不再看第二个值。


def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


print(any_lowercase4('AbC'))


def any_lowercase5(s):
    for c in s:
        if c.islower():
            return True
    return False


print(any_lowercase5('AbC'))
