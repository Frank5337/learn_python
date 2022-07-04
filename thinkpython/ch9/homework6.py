# Email: zbl5337@gmail.com
# Create by Frozen
# Date: 2022/7/4 10:26


def is_abcdedarian(word, ss):
    if len(ss) > len(word):
        return -1
    index = 0
    len_ss = len(ss)
    len_word = len(word) - len_ss
    res = 0
    while index <= len_word:
        if word[index: index + len_ss] == ss:
            res = res + 1
        index = index + 1
    return res


print(is_abcdedarian('wykabcwykqwewyk', 'wyk'))

