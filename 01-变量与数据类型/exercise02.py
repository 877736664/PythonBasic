"""
01-变量与数据类型 - 练习2
练习目标：掌握类型转换
"""

# 1. 字符串转数字
num_str = "123"
# 将num_str转换为整数，保存到变量num_int中
# 请在这里写下你的代码
num_int = int(num_str)

# print(num_int)
# print(type(num_int))

print(f"num_int = {num_int}, 类型是 {type(num_int)}")

# 2. 数字转字符串
price = 99.5
# 将price转换为字符串，保存到price_str中
# 请在这里写下你的代码
price_str = str(price)

print(f"price_str = {price_str}, 类型是 {type(price_str)}")

# 3. 输入计算
# 用户输入两个数字，计算它们的和
# 提示：input()返回的是字符串，需要转换类型
num1 = input("请输入第一个数字：")
num2 = input("请输入第二个数字：")

# 计算两个数的和，保存到result中
# 请在这里写下你的代码

result = float(num1) + float(num2)

print(f"两个数的和是：{result}")
