# Email: zbl5337@gmail.com
# Create by Frozen
# Date: 2022/7/5 9:36


def has_duplicates(t):
    temp = t[:]
    for x in range(len(temp)):
        for y in range(len(temp)):
            if temp[x] == temp[y] and x != y:
                return True
    return False


print(has_duplicates([1, 2, 3, 4]))
print(has_duplicates([1, 2, 3, 4, 4]))

