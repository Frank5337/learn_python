# Email: zbl5337@gmail.com
# Create by Frozen
# Date: 2022/7/3 22:43

fruit = 'banana'
letter = fruit[0 + 1]

print(letter)

print(len(letter))

print('========')

index = 0

while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1

print('========')

for letter in fruit:
    print(letter)

# 字符串切片
# 字符串的一个片段被称作 切片 (slice) 。选择一个切片的操作类似于选择一个字符
s = 'Monty Python'
print(s[0:5])

print(s[6:12])


# Traceback (most recent call last):
#   File "D:\develop\GoProjects\helloworld\thinkpython\ch8\test1.py", line 34, in <module>
#     greeting[0] = 'J'
# TypeError: 'str' object does not support item assignment
# 字符串是不可变的
# greeting = 'Hello world'
# greeting[0] = 'J'


def find(word, l):
    idx = 0
    while idx < len(word):
        if word[idx] == l:
            return idx
        idx = idx + 1
    return -1


print(find('abcdefg', 'b'))


