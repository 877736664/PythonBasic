"""
01-变量与数据类型 - 练习1
练习目标：掌握变量定义和基本数据类型
"""

# 1. 定义不同类型的变量
# 请定义一个整数变量age，值为25
# 请定义一个浮点数变量height，值为175.5
# 请定义一个字符串变量name，值为"张三"
# 请定义一个布尔变量is_student，值为True

# 请在这里写下你的代码
age = 25
height = 175.5
name = "张三"
is_student = True

# 2. 打印变量及其类型
# 使用print()打印每个变量的值
# 使用type()函数打印每个变量的类型
# 例如：print(name, type(name))

# 请在这里写下你的代码
print(age, type(age))
print(height, type(height))
print(name, type(name))
print(is_student, type(is_student))

# 3. 变量交换
a = 10
b = 20
# 不使用第三个变量，交换a和b的值
# 交换后a应该是20，b应该是10

# 请在这里写下你的代码
a = a + b   # 30
b = a - b   # 10
a = a - b   # 20

print(f"交换后 a = {a}, b = {b}")
