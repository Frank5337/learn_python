# Email: zbl5337@gmail.com
# Create by Frozen
# Date: 2022/7/1 9:31
import turtle

bob = turtle.Turtle()


def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360 / n)


polygon(bob, 200, 6)

turtle.mainloop()
