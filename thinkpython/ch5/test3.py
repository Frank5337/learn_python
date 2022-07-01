# Email: zbl5337@gmail.com
# Create by Frozen
# Date: 2022/7/1 14:40

def is_triangle(x, y, z):
    if x + y < z:
        print('No')
        return
    if x + z < y:
        print('No')
        return
    if y + z < x:
        print('No')
        return
    print('Yes')


input1 = int(input('请输入a:'))
input2 = int(input('请输入b:'))
input3 = int(input('请输入c:'))

is_triangle(input1, input2, input3)
