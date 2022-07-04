# Email: zbl5337@gmail.com
# Create by Frozen
# Date: 2022/7/4 10:23


def uses_all(word, contains):
    res = True
    for s in contains:
        res = word.__contains__(s) and res
    return res


print(uses_all('abcdefghijklou', 'aeiou'))
print(uses_all('abcdefg', 'aeiou'))
