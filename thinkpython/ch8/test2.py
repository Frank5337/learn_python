# Email: zbl5337@gmail.com
# Create by Frozen
# Date: 2022/7/3 23:05

def find(word, l, start):
    idx = 0
    idx = idx + start
    while len(word) > idx:
        if word[idx] == l:
            return idx
        idx = idx + 1
    return -1


print(find('abcdefg', 'f', 3))

word = 'banana'
new_word = word.upper()
print(new_word)