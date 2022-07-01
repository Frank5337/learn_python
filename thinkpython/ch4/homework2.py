# Email: zbl5337@gmail.com
# Create by Frozen
# Date: 2022/7/1 9:31
import turtle

bob = turtle.Turtle()


def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


square(bob, 200)

turtle.mainloop()
