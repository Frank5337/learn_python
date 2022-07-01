# Email: zbl5337@gmail.com
# Create by Frozen
# Date: 2022/7/1 15:47

def a(m, n):
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return a(m - 1, 1)
    if m > 0 and n > 0:
        return a(m - 1, a(m, n - 1))


print(a(3, 4))

# m n 较大时 递归层数指数递增
# RecursionError: maximum recursion depth exceeded in comparison
# 超过最大递归层数
# print(a(30, 40))
