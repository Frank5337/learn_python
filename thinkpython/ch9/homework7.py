# Email: zbl5337@gmail.com
# Create by Frozen
# Date: 2022/7/4 14:07

def find_tribe(word):
    if len(word) < 6:
        return False
    index = 0
    while index < len(word) - 6:
        if word[index] == word[index + 1] and word[index + 2] == word[index + 3] and word[index + 4] == word[index + 5]:
            return True
        index = index + 1
    return False


print(find_tribe('committee'))
print(find_tribe('Mississippi'))
print(find_tribe('Mississippi'.replace('i', 's')))
