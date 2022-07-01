# Email: zbl5337@gmail.com
# Create by Frozen
# Date: 2022/7/1 9:31
import math
import turtle

bob = turtle.Turtle()


def left(t, length, n, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle / n)


def right(t, length, n, angle):
    t.rt(180)
    for i in range(n):
        t.fd(length)
        t.rt(angle / n)


def flower(t, length, n, angle):
    left(t, length, n, angle)
    t.rt(180 + angle)
    left(t, length, n, angle)


def flower2(t, length, n, angle, x, y):
    for i in range(x):
        flower(t, length, n, angle / x)
        t.lt(angle / y)


flower2(bob, 10, 20, 360, 24, 20)
bob.rt(360 / 24 / 2)
flower2(bob, 10, 10, 360, 24, 10)

turtle.mainloop()
