# Email: zbl5337@gmail.com
# Create by Frozen
# Date: 2022/7/4 18:12


def is_sorted(t):
    index = 1
    while index < len(t):
        if t[index - 1] > t[index]:
            return False
        index += 1
    return True


print(is_sorted([1, 2, 2]))

print(is_sorted(['b', 'a']))

