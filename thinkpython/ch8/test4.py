# Email: zbl5337@gmail.com
# Create by Frozen
# Date: 2022/7/3 23:29


def count(str, x):
    index = 0
    counter = 0
    while index < len(str):
        if str[index] == x:
            counter = counter + 1
        index = index + 1
    return counter


print(count('banana', 'a'))

fruit = 'banana'
print(fruit[0:5:2])
print(fruit[0:3:1])
print(fruit[0:5:3])
print(fruit[0:4:2])

print('=========')
fruit = 'banana'
print(fruit[::-1])