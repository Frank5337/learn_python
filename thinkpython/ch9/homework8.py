# Email: zbl5337@gmail.com
# Create by Frozen
# Date: 2022/7/4 15:16


def hui_wen(s1):
    if len(s1) == 0 or len(s1) == 1:
        return True
    if s1[0] == s1[len(s1) - 1]:
        res = hui_wen(s1[1:-1])
        return res
    return False


print(hui_wen('110011'))

index = 100000
while index < 999999:
    s = str(index)
    # if s[0] == s[5] and s[1] == s[4] and s[2] == s[3]:
    if hui_wen(s):
        print(index)
    index = index + 1
