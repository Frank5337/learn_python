# Email: zbl5337@gmail.com
# Create by Frozen
# Date: 2022/7/1 9:31
import math
import turtle

bob = turtle.Turtle()


def general(t, r, angle):
    circle(t, r, angle)


def circle(t, r, angle):
    length = 2 * math.pi * r / 360
    polygon(t, length, 360, angle)


def polygon(t, length, n, angle):
    for i in range(angle):
        t.fd(length)
        t.lt(360 / n)


general(bob, 200, 180)

turtle.mainloop()
