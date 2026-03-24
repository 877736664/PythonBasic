"""
12-模块与包 - 练习1
练习目标：掌握导入和自定义模块
"""

# 1. 导入练习
# 请导入 math 模块，计算：
# - 圆面积 radius=5，公式 π * r²
# - sqrt(16) 开平方
# 请写下代码

import

radius = 5
area =
print(f"半径5的圆面积：{area:.2f}")

sqrt_16 =
print(f"16的平方根：{sqrt_16}")
print("-" * 30)

# 2. 从math导入pi和sqrt
from math import
# 重新计算一遍，结果和上面一样

area2 =
sqrt_16_2 =
print(f"area2 = {area2:.2f}")
print(f"sqrt_16_2 = {sqrt_16_2}")
print("-" * 30)

# 3. 自定义模块
# 在同目录创建一个 utils.py，里面写两个函数：
# def add(a, b): 返回a+b
# def multiply(a, b): 返回a*b
# 然后在这里导入utils，调用它们
# 请完成这个练习

# 先写 utils.py 再导入
# from utils import add, multiply

# 测试：
# print(add(3, 5))
# print(multiply(4, 6))
