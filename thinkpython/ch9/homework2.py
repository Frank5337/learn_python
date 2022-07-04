# Email: zbl5337@gmail.com
# Create by Frozen
# Date: 2022/7/4 9:54

file = open('D:\work\PycharmProjects\learn_python//thinkpython\ch9\words.txt')
# print(file.readline())
# print(file.readline())
# print(file.readline())


def has_no_e(w):
    for s in w:
        if s == 'e':
            return False
    return True


for line in file:
    word = line.strip()
    if(len(word)) > 20 and has_no_e(word):
        print(word)





