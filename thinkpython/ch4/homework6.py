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


for i in range(6):
    flower(bob, 20, 10, 60)
    bob.lt(60)

turtle.mainloop()
