# Email: zbl5337@gmail.com
# Create by Frozen
# Date: 2022/7/4 9:54


# print(file.readline())
# print(file.readline())
# print(file.readline())


def uses_only(word, st):
    wb = True
    for s in st:
        wb = word.__contains__(s) and wb
    return wb


print(uses_only('Frozen', 'eno'))
print(uses_only('Frozen', 'enoX'))

