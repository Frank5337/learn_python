# Email: zbl5337@gmail.com
# Create by Frozen
# Date: 2022/7/4 18:16


def is_anagram(word1, word2):
    if len(word1) != len(word2):
        return False
    # 数组拷贝
    temp = word2[:]
    for x in word1:
        temp.remove(x)
    if len(temp) == 0:
        return True
    return False


w2 = [2, 3, 1]
print(is_anagram([1, 2, 3], w2))

# 2空了
print(w2)
