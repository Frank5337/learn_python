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


def avoids(w, ban):
    for s in w:
        for b in ban:
            if s == b:
                return False
    return True


def find(ban):
    for line in file:
        word = line.strip()
        # if (len(word)) > 20 and has_no_e(word):
        #     print(word)
        strip = word.split(' ')
        for s in strip:
            if avoids(s, ban):
                print(s)


ban_str = input('请输入一个禁止使用的字符')
find(ban_str)

