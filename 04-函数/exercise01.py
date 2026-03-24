"""
04-函数 - 练习1
练习目标：掌握函数定义和调用
"""

# 1. 定义一个函数，计算两个数的和
def add(a, b):
    return a + b

# 测试
print(f"add(3, 5) = {add(3, 5)}")
print(f"add(10, 20) = {add(10, 20)}")

# 2. 定义一个函数，判断一个数是否是偶数
def is_even(n):
    # 如果是偶数返回True，否则返回False
    # 请在这里补充代码
    return n % 2 == 0

# 测试
print(f"is_even(4) = {is_even(4)}")
print(f"is_even(7) = {is_even(7)}")

# 3. 定义一个函数，计算圆的面积
import math
def circle_area(radius):
    # 公式：π * r²，可以使用math.pi
    # 请在这里补充代码
    return math.pi * (radius ** 2)

# 测试
print(f"半径为5的圆面积：{circle_area(5):.2f}")

# 4. 定义一个函数，判断年份是否是闰年
def is_leap_year(year):
    # 返回True如果是闰年，否则False
    # 闰年规则：能被4整除但不能被100整除，或者能被400整除
    # 请在这里补充代码
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


# 测试
print(f"2024是否闰年：{is_leap_year(2024)}")
print(f"2023是否闰年：{is_leap_year(2023)}")
print(f"2000是否闰年：{is_leap_year(2000)}")
print(f"1900是否闰年：{is_leap_year(1900)}")
