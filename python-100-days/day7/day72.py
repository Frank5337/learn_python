print('除了上面提到的生成器语法，Python中还有另外一种定义生成器的方式，'
      '就是通过yield关键字将一个普通函数改造成生成器函数。'
      '下面的代码演示了如何实现一个生成斐波拉切数列的生成器。'
      '所谓斐波拉切数列可以通过下面递归的方法来进行定义：')

print('$${\displaystyle F_{0}=0}$$')

print('$${\displaystyle F_{1}=1}$$')

print('$${\displaystyle F_{n}=F_{n-1}+F_{n-2}}({n}\geq{2})$$')


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a  # 把a当成list yield => a = list.add(a)


def main():
    for val in fib(20):
        print(val)


if __name__ == '__main__':
    main()
