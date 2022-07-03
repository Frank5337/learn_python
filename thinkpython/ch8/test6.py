# Email: zbl5337@gmail.com
# Create by Frozen
# Date: 2022/7/3 23:45


def rotate_word(word, num):
    index = 0
    res = ''
    while index < len(word):
        res = res + chr(ord(word[index]) + num)
        index = index + 1
    return res


print(rotate_word('cheer', 7))
