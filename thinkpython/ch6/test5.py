# Email: zbl5337@gmail.com
# Create by Frozen
# Date: 2022/7/1 21:00


def is_power(a, b):
    if a / b == b * b:
        return True
    return False


print(is_power(4, 2))
print(is_power(8, 2))
print(is_power(8, 4))
print(is_power(16, 4))
