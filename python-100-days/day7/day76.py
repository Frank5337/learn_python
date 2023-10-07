# popitem()
# 从字典中移除并返回一个 (键, 值) 对。 键值对会按 LIFO 的顺序被返回。
#
# popitem() 适用于对字典进行消耗性的迭代，这在集合算法中经常被使用。 如果字典为空，调用 popitem() 将引发 KeyError。
#
# 在 3.7 版更改: 现在会确保采用 LIFO 顺序。 在之前的版本中，popitem() 会返回一个任意的键/值对。

scores = {'张三': 90, '李四': 85, '王五': 95}

item = scores.popitem()
print(item)  # 输出：('王五', 95)