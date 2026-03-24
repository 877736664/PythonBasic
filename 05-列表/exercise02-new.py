"""
05-列表 - 新练习题
练习目标：巩固列表基本操作、常用方法、遍历
"""

# ========== 练习1：列表创建与访问 ==========
# 要求：
# 1. 创建一个列表 names，包含 "张三", "李四", "王五", "赵六" 四个人名
# 2. 打印第一个人名
# 3. 打印最后一个人名（使用负索引）
# 4. 打印列表长度
# 请写下你的代码

names = ["张三", "李四", "王五", "赵六"]
print("第一个人名：", names[0])       # 你的代码
print("最后一个人名：", names[-1])     # 你的代码
print("列表长度：", len(names))         # 你的代码

print("-" * 30)




# ========== 练习2：切片操作 ==========
data = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
# 要求：
# 1. 获取前 5 个元素 → result1
# 2. 获取索引 3 到索引 7 的元素（包含7） → result2
# 3. 获取所有奇数位置的元素（步长2，从索引1开始） → result3
# 4. 反转列表 → result4
# 请写下你的代码

result1 = data[:5]
print(f"前5个元素：{result1}")

result2 = data[3:8]
print(f"索引3到7：{result2}")

result3 = data[1::2]
print(f"奇数位置：{result3}")

result4 = data[::-1]
print(f"反转后：{result4}")

print("-" * 30)


# ========== 练习3：增删改元素 ==========
colors = ["红色", "绿色", "蓝色"]
print(f"初始：{colors}")
# 要求：
# 1. 在末尾添加 "黄色"
# 2. 在索引 1 的位置插入 "紫色"
# 3. 修改索引 2 的位置为 "黑色"
# 4. 删除最后一个元素
# 5. 删除索引 0 的元素
# 请写下你的代码
colors.append("黄色")
colors.insert(1, "紫色")
colors[2] = "黑色"
colors.pop()
colors.pop(0)

# （完成后打印看看结果）
print(f"操作后：{colors}")

print("-" * 30)





# ========== 练习4：列表推导式 ==========
# 要求：
# 1. 生成 1-10 每个数的立方 → cubes （立方是 x**3）
# 2. 生成 1-30 之间所有 3 的倍数 → multiples
# 3. 把字符串列表 "hello", "world", "python" 每个单词转成大写 → 用列表推导式

words = ["hello", "world", "python"]

cubes = [x**3 for x in range(1, 11)]
print(f"1-10的立方：{cubes}")

multiples = [x for x in range(1, 31) if x % 3 == 0]
print(f"1-30中3的倍数：{multiples}")

upper_words = [words.upper() for words in words]
print(f"转大写后：{upper_words}")

print("-" * 30)

# ========== 练习5：统计个数 ==========
# 统计列表中大于等于 60 的元素有多少个
scores = [85, 59, 92, 45, 78, 60, 55, 88]
count = 0  # 计数器

# 请遍历列表，统计大于等于60的个数
# 代码写这里
for s in scores:
    if s >= 60:
        count += 1

print(f"大于等于60的分数有 {count} 个")

print("-" * 30)


# ========== 练习6：去重并保持原来顺序 ==========
# 题目：列表去重，但要求保持元素第一次出现的顺序
# 提示：新建一个空列表，遍历原列表，如果元素不在新列表中才添加
arr = [2, 1, 3, 2, 4, 1, 5, 3]
unique_arr = []  # 结果存在这里

# 请写下你的代码
for item in arr:
    if item not in unique_arr:
        unique_arr.append(item)

print(f"去重后（保持顺序）：{unique_arr}")
