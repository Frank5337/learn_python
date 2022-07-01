# Email: zbl5337@gmail.com
# Create by Frozen
# Date: 2022/7/1 9:31
import math
import turtle

bob = turtle.Turtle()


def circle(t, r):
    length = 2 * math.pi * r / 360
    polygon(t, length, 360)


def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360 / n)


circle(bob, 50)

turtle.mainloop()
