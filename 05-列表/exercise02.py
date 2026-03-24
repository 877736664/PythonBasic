"""
05-列表 - 练习2
练习目标：掌握列表常用方法和遍历
"""

# 1. 对列表排序
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
# 升序排序（原地排序）
# 请在这里写下你的代码
numbers.sort()
print(f"升序排序：{numbers}")

# 降序排序
# 请在这里写下你的代码
numbers.sort(reverse=True)
print(f"降序排序：{numbers}")




# 2. 列表推导式练习
# 生成1-10每个数的平方组成的列表
# 使用列表推导式
# ========== 解题思路 ==========
# 列表推导式格式：[表达式 for 变量 in 范围]
# 表达式就是 i 的平方 → i * i 或者 i ** 2
# range(1, 11) 包含1到10
squares = [i ** 2 for i in range(1, 11)]
print(f"1-10的平方：{squares}")

# 生成1-20之间所有偶数组成的列表
# ========== 解题思路 ==========
# 加上条件判断 → [表达式 for 变量 in 范围 if 条件]
# 条件：i % 2 == 0 就是偶数
evens = [i for i in range(1, 21) if i % 2 == 0]
print(f"1-20之间的偶数：{evens}")




# 3. 将列表中所有元素去重
original = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6]
# 去重后保存到unique_list
# 提示：可以使用set转换再转回list
# ========== 解题思路 ==========
# 集合set本身特性就是不允许重复元素，所以转成set自动去重，再转回list就行
unique_list = list(set(original))
# 注意：set是无序的，如果想保持原来顺序，可以用其他方法，题目没要求顺序的话这个方法最简单
print(f"去重后：{unique_list}")




# 4. 找出列表中的最大值和最小值（不使用内置函数max/min）
nums = [3, 1, 4, 1, 5, 9, 2, 6]
# 手动遍历找最大值最小值
max_val = nums[0]
min_val = nums[0]

# 请在这里遍历并计算
# 不要用内置的max()和min()函数
# ========== 解题思路 ==========
# 1. 先假设第一个元素就是最大/最小值（已经写好了）
# 2. 遍历列表中每一个元素
# 3. 如果当前元素比max_val大，就更新max_val
# 4. 如果当前元素比min_val小，就更新min_val
for num in nums:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num

print(f"最大值：{max_val}, 最小值：{min_val}")

# 5. 将两个列表合并成一个有序列表
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
# 合并后排序
# ========== 解题思路 ==========
# 列表用 + 就可以合并，然后排序即可
merged = list1 + list2
merged.sort()
print(f"合并排序后：{merged}")
