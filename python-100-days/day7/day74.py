# 创建集合的字面量语法
set1 = {1, 2, 3, 3, 3, 2}
print(set1)
print('Length =', len(set1))
# 创建集合的构造器语法(面向对象部分会进行详细讲解)
set2 = set(range(1, 10))
set3 = set((1, 2, 3, 3, 2, 1))
print(set2, set3)
# 创建集合的推导式语法(推导式也可以用于推导集合)
set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
print(set4)

# 向集合添加元素和从集合删除元素。
print('向集合添加元素和从集合删除元素')
set1.add(4)
set1.add(5)
print(set1)
print(set2)
set2.update([11, 12])  # set2 + [11,12]
print(set2)
set2.discard(5)  # set2 移除5
set2.discard(12)
print(set2)
if 4 in set2:
    set2.remove(4)
print(set1, set2)
print(set3.pop())
print(set3)

# 集合的成员、交集、并集、差集等运算。

print('集合的交集、并集、差集、对称差运算')
print(set1 & set2) # 交集
# print(set1.intersection(set2))
print(set1 | set2) # 并集
# print(set1.union(set2))
print(set1 - set2) # 差集
# print(set1.difference(set2))
print(set1 ^ set2)
# print(set1.symmetric_difference(set2))
# 判断子集和超集
print(set2 <= set1)
# print(set2.issubset(set1))
print(set3 <= set1)
# print(set3.issubset(set1))
print(set1 >= set2)
# print(set1.issuperset(set2))
print(set1 >= set3)
# print(set1.issuperset(set3))
# 说明： Python中允许通过一些特殊的方法来为某种类型或数据结构自定义运算符（后面的章节中会讲到），
# 上面的代码中我们对集合进行运算的时候可以调用集合对象的方法，也可以直接使用对应的运算符，
# 例如&运算符跟intersection方法的作用就是一样的，但是使用运算符让代码更加直观。