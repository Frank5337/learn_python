# Email: zbl5337@gmail.com
# Create by Frozen
# Date: 2022/7/1 0:19

a = '+ ' + '- ' * 4
b = '| ' + '  ' * 4

print(a + a + '+')
print(b + b + '|')
print(b + b + '|')
print(b + b + '|')
print(b + b + '|')
print(a + a + '+')
print(b + b + '|')
print(b + b + '|')
print(b + b + '|')
print(b + b + '|')
print(a + a + '+')

print("=====================")


def do_twice(f):
    f()
    f()


def do_four(f):
    do_twice(f)
    do_twice(f)


def print_beam():
    # print 函数默认会自动换行，但是你可以阻止这个行为，只需要像下面这样将行结尾变成一个空格：
    print('+ - - - -', end=' ')


def print_post():
    print('|        ', end=' ')


def print_beams():
    do_twice(print_beam)
    print('+')


def print_posts():
    do_twice(print_post)
    print('|')


def print_row():
    print_beams()
    do_four(print_posts)


def print_grid():
    do_twice(print_row)
    print_beams()


print_grid()
