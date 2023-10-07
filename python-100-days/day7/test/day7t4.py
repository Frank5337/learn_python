# 练习4：设计一个函数返回传入的列表中最大和第二大的元素的值。
# 参考答案：


def getMax2(l):
    l.sort()
    return l[len(l) - 1], l[len(l) - 2]


def getMax22(l):
    m1, m2 = (l[0], l[1]) if l[0] > l[1] else (l[1], l[0])
    for index in range(2, len(l)):
        if l[index] > m1:
            m2 = m1
            m1 = l[index]
        elif l[index] > m2:
            m2 = l[index]
    return m1, m2


if __name__ == '__main__':
    l1 = [1, 3, 5, 11, 12, 18, 9, 10]
    print(getMax2(l1))
    print(getMax22(l1))
