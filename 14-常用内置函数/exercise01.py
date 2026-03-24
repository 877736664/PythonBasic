"""
14-常用内置函数 - 练习1
练习目标：掌握常用内置函数
"""

# 1. 数学练习
nums = [3, 1, 4, 1, 5, 9, 2, 6]
# 使用内置函数求：最大值、最小值、总和、长度
# 请写下代码

max_num =
min_num =
total =
length =

print(f"最大值：{max_num}")
print(f"最小值：{min_num}")
print(f"总和：{total}")
print(f"长度：{length}")
print("-" * 30)

# 2. enumerate 使用
# 遍历列表，打印 "行号: 内容"，行号从1开始
words = ["hello", "world", "python"]
# 使用enumerate
# 请写下代码


print("-" * 30)

# 3. zip 使用
# 两个列表，names 和 scores，把它们配对打印
# 格式：张三: 85, 李四: 92...
names = ["张三", "李四", "王五"]
scores = [85, 92, 78]
# 用zip遍历
# 请写下代码


print("-" * 30)

# 4. sorted 练习
# 把 nums 按升序排序，再按降序排序
nums = [3, 1, 4, 1, 5, 9, 2, 6]

asc =
desc =

print(f"升序：{asc}")
print(f"降序：{desc}")
print("-" * 30)

# 5. map 练习
# 把列表 [1, 2, 3, 4, 5] 每个元素平方，得到新列表
# 使用map
nums = [1, 2, 3, 4, 5]

squares =
# 转成list看看结果
print(f"平方后：{list(squares)}")
print("-" * 30)

# 6. filter 练习
# 过滤出列表中大于等于60的元素
nums = [85, 59, 92, 45, 78, 60, 55, 88]

passed =

print(f"大于等于60：{list(passed)}")
