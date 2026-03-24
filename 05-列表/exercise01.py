"""
05-列表 - 练习1
练习目标：掌握列表基本操作：增删改查
"""

# 1. 创建一个包含5个元素的列表，然后打印
# 请创建一个包含1, 3, 5, 7, 9的列表my_list
my_list =  [1, 3, 5, 7, 9]# 请在这里补充代码

print(f"my_list = {my_list}")

# 2. 访问列表元素
# 打印第一个元素
# 打印最后一个元素（使用负索引）
# 打印索引位置2的元素
# 请在这里写下你的代码
print(f"my_list[0] = {my_list[0]}")
print(f"my_list[-1] = {my_list[-1]}")
print(f"my_list[2] = {my_list[2]}")


# 3. 切片操作
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 获取前3个元素 → [0, 1, 2]
# 获取索引2到索引5的元素 → [2, 3, 4, 5]
# 获取偶数位置的元素（步长为2）
# 反转整个列表
# 请在这里写下你的代码

first_three = numbers[:3]
print(f"前3个元素：{first_three}")

index_2_to_5 = numbers[2:6]
print(f"索引2到5：{index_2_to_5}")

even_positions = numbers[::2]
print(f"偶数位置：{even_positions}")

reversed_list = numbers[::-1]
print(f"反转后：{reversed_list}")

# 4. 增删元素
fruits = ["苹果", "香蕉", "橙子"]
print(f"初始：{fruits}")

# 在末尾添加"葡萄"
# 请写下代码
fruits.append("葡萄")

# 在索引1位置插入"草莓"
# 请写下代码
fruits.insert(1, "草莓")

print(f"添加后：{fruits}")

# 删除最后一个元素
# 请写下代码
fruits.pop()

# 删除索引0位置的元素
# 请写下代码
fruits.pop(0)

print(f"删除后：{fruits}")

# 5. 查找元素
scores = [85, 92, 78, 92, 65, 92]
# 查找92在列表中第一次出现的索引
# 统计92在列表中出现的次数
# 请在这里写下你的代码
first_index = scores.index(92)
count = scores.count(92)

print(f"92在列表中第一次出现的索引", first_index)
print(f"92在列表中出现的次数", count)