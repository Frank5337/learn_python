a = 321
b = 12
print(a + b)  # 333
print(a - b)  # 309
print(a * b)  # 3852
print(a / b)  # 26.75

a = 100
b = 12.345
c = 1 + 5j
d = 'hello, world'
e = True
print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'complex'>
print(type(d))  # <class 'str'>
print(type(e))  # <class 'bool'>

radius = float(input('请输入圆的半径: '))
# 2Πr
perimeter = 2 * 3.1416 * radius
area = 3.1416 * radius ** 2
area2 = 3.1416 * radius * radius
print('周长: ', perimeter)
print('面积: ', area)
print('面积: ', area2)

"""
输入年份 如果是闰年输出True 否则输出False
"""

year = int(input('请输入年份: '))
check = year % 4 == 0
print(check)
