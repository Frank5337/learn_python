# Email: zbl5337@gmail.com
# Create by Frozen
# Date: 2022/7/4 15:38


def check(s1, s2):
    if len(s1) == len(s2) and len(s1) == 2:
        return s1[0] == s2[1] and s2[0] == s1[1]
    return False


mom = 120
# 99 63 98 62 96 60
i = mom - (73 - 37)

while mom >= 73 - 37 + 10:
    if check(str(i), str(mom)):
        print(i, mom)
    i = i - 1
    mom = mom - 1


if 1 > 0:
    print(1)
elif 2 > 1:
    print(2)