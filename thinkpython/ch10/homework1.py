# Email: zbl5337@gmail.com
# Create by Frozen
# Date: 2022/7/4 18:04

def nested_sum(tt):
    total = 0
    for x in tt:
        total += sum(x)
    return total


t = [[1, 2], [3], [4, 5, 6]]
print(nested_sum(t))
