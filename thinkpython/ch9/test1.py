# Email: zbl5337@gmail.com
# Create by Frozen
# Date: 2022/7/4 9:54

file = open('D:\work\PycharmProjects\learn_python//thinkpython\ch9\words.txt')
# print(file.readline())
# print(file.readline())
# print(file.readline())

for line in file:
    word = line.strip()
    print(word)