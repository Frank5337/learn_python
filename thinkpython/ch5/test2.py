# Email: zbl5337@gmail.com
# Create by Frozen
# Date: 2022/7/1 14:26


def check_fermat(a, b, c, n):
    if a ** n + b ** n == c ** n:
        print('Holy smokes, Fermat was wrong')
    else:
        print('No, that doesn\'t work')


input1 = int(input('请输入a:'))
input2 = int(input('请输入b:'))
input3 = int(input('请输入c:'))
input4 = int(input('请输入n:'))

check_fermat(input1, input2, input3, input4)
