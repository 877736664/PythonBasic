"""
06-元组 - 练习1
练习目标：掌握元组创建和基本操作
"""

# 1. 创建元组
# 请创建：
# - 一个空元组 empty
# - 一个包含三个颜色"红","绿","蓝"的元组 colors
# - 一个单元素元组，值是100 single
# 请在这里写下代码

empty = ()
colors = ("红","绿","蓝")
single = (100,)

print(f"empty = {empty}")
print(f"colors = {colors}")
print(f"single = {single}, 类型是 {type(single)}")
print("-" * 30)

# 2. 元组索引和切片
nums = (10, 20, 30, 40, 50)
# 打印第一个元素
# 打印最后一个元素（负索引）
# 切片获取索引1到3的元素（包含3）
# 请写下代码

print(f"第一个元素：", nums[0])  # 补充完整
print(f"最后一个元素：", nums[-1])
print(f"索引1-3：", nums[1:4])

print("-" * 30)

# 3. 元组解包
# 有元组 info = ("张三", 18, "北京")
# 使用解包把三个值分别赋值给 name, age, city
info = ("张三", 18, "北京")

# 请在这里写下代码
name, age, city = info

print(f"name = {name}")
print(f"age = {age}")
print(f"city = {city}")

print("-" * 30)

# 4. *解包技巧
# 把列表第一个元素给a，最后一个元素给c，中间所有元素给b
numbers = [1, 2, 3, 4, 5]

# 请使用*解包
# a = 第一个, b = 中间列表, c = 最后一个
a, *b, c = [1, 2, 3, 4, 5]


print(f"a = {a}, b = {b}, c = {c}")
