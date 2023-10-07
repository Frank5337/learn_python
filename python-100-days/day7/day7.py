s1 = 'hello, world!'
s2 = "hello, world!"
# 以三个双引号或单引号开头的字符串可以折行
s3 = """
hello, 
world!
"""
s4 = 'hala'
print(s1, s2, s3, s4, end='')

# 可以在字符串中使用\（反斜杠）来表示转义，也就是说\后面的字符不再是它原来的意义，
# 例如：\n不是代表反斜杠和字符n，而是表示换行；而\t也不是代表反斜杠和字符t，而是表示制表符。
# 所以如果想在字符串中表示'要写成\'，同理想表示\要写成\\。可以运行下面的代码看看会输出什么。
s1 = '\'hello, world!\''
s2 = '\n\\hello, world!\\\n'
print(s1, s2, end='')

s1 = '\141\142\143\x61\x62\x63'
s2 = '\u9a86\u660a'
print(s1, s2)

# 如果不希望字符串中的\表示转义，我们可以通过在字符串的最前面加上字母r来加以说明，再看看下面的代码又会输出什么。
s1 = r'\'hello, world!\''
s2 = r'\n\\hello, world!\\\n'
print(s1, s2, end='')

# ython为字符串类型提供了非常丰富的运算符，
# 我们可以使用+运算符来实现字符串的拼接，
# 可以使用*运算符来重复一个字符串的内容，
# 可以使用in和not in来判断一个字符串是否包含另外一个字符串（成员运算），
# 我们也可以用[]和[:]运算符从字符串取出某个字符或某些字符（切片运算），代码如下所示。

s1 = 'hello ' * 3
print(s1)  # hello hello hello
s2 = 'world'
s1 += s2
print(s1)  # hello hello hello world
print('ll' in s1)  # True
print('good' in s1)  # False
str2 = 'abc123456'
# 从字符串中取出指定位置的字符(下标运算)
print(str2[2])  # c
# 字符串切片(从指定的开始索引到指定的结束索引)
print(str2[2:5])  # c12 包头不包尾
print(str2[2:])  # c123456
print(str2[2::2])  # c246
print(str2[::2])  # ac246
print(str2[::-1])  # 654321cba
print(str2[-3:-1])  # 45

# 在Python中，我们还可以通过一系列的方法来完成对字符串的处理，代码如下所示。

str1 = 'hello, world!'
# 通过内置函数len计算字符串的长度
print(len(str1))  # 13
# 获得字符串首字母大写的拷贝
print(str1.capitalize())  # Hello, world!
# 获得字符串每个单词首字母大写的拷贝
print(str1.title())  # Hello, World!
# 获得字符串变大写后的拷贝
print(str1.upper())  # HELLO, WORLD!
# 从字符串中查找子串所在位置
print(str1.find('or'))  # 8
print(str1.find('shit'))  # -1
print(str1.find('o'))  # 4
# 与find类似但找不到子串时会引发异常
# print(str1.index('or'))
# print(str1.index('shit'))
# 检查字符串是否以指定的字符串开头
print(str1.startswith('He'))  # False
print(str1.startswith('hel'))  # True
# 检查字符串是否以指定的字符串结尾
print(str1.endswith('!'))  # True
# 将字符串以指定的宽度居中并在两侧填充指定的字符
print(str1.center(50, '*'))
# 将字符串以指定的宽度靠右放置左侧填充指定的字符
print(str1.rjust(50, ' '))
str2 = 'abc123456'
# 检查字符串是否由数字构成
print(str2.isdigit())  # False
# 检查字符串是否以字母构成
print(str2.isalpha())  # False
# 检查字符串是否以数字和字母构成
print(str2.isalnum())  # True
str3 = '  jackfrued@126.com '
print(str3)
# 获得字符串修剪左右两侧空格之后的拷贝
print(str3.strip())


# 可以用下面的方式来格式化输出字符串。

a, b = 5, 10
print('%d * %d = %d' % (a, b, a * b))
# 当然，我们也可以用字符串提供的方法来完成字符串的格式，代码如下所示。

a, b = 5, 10
print('{0} * {1} = {2}'.format(a, b, a * b))
# Python 3.6以后，格式化字符串还有更为简洁的书写方式，就是在字符串前加上字母f，我们可以使用下面的语法糖来简化上面的代码。

a, b = 5, 10
print(f'{a} * {b} = {a * b}')
# 除了字符串，Python还内置了多种类型的数据结构，如果要在程序中保存和操作数据，
# 绝大多数时候可以利用现有的数据结构来实现，最常用的包括列表、元组、集合和字典。


