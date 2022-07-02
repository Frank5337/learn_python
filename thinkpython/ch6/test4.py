# Email: zbl5337@gmail.com
# Create by Frozen
# Date: 2022/7/1 16:01


def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]


def is_palindrome(str):
    if len(str) == 0:
        return True
    if len(str) == 1:
        return False
    if first(str) != last(str):
        return False
    return is_palindrome(middle(str))


# print(is_palindrome('aabsbaa'))

def is_palindrome1(word):
    """Returns True if word is a palindrome."""
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))


print(is_palindrome('allen'))
print(is_palindrome1('allen'))
print(is_palindrome('bob'))
print(is_palindrome1('bob'))
print(is_palindrome('otto'))
print(is_palindrome1('otto'))
print(is_palindrome('redivider'))
print(is_palindrome1('redivider'))