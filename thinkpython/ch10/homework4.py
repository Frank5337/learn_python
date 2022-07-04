# Email: zbl5337@gmail.com
# Create by Frozen
# Date: 2022/7/4 18:10


def chop(tt):
    # tt.pop(0)
    # tt.pop(-1)
    del tt[0]
    del tt[-1]


t = [1, 2, 3, 4]
chop(t)
print(t)
