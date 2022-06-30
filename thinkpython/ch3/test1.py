# Email: zbl5337@gmail.com
# Create by Frozen
# Date: 2022/7/1 0:13

def right_justify(s):
    print(" " * 70, s)


right_justify('monty')


def do_twice(f):
    f()
    f()


def print_spam():
    print('spam')

    do_twice(print_spam)


def do_twice2(func, aa):
    func(aa)


#do_twice2(print_spam, "aa")
do_twice2(print, "aa")
