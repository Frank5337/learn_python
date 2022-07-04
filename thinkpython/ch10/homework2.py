# Email: zbl5337@gmail.com
# Create by Frozen
# Date: 2022/7/4 18:07

def cum_sum(tt):
    res = []
    curr = 0
    for x in tt:
        curr += x
        res.append(curr)
    return res


t = [1, 2, 3]
print(cum_sum(t))

