"""
02-运算符 - 练习1
练习目标：掌握算术运算符
"""

# 1. 算术运算练习
a = 10
b = 3

# 计算并打印：
# 加法 a + b
# 减法 a - b
# 乘法 a * b
# 除法 a / b
# 整除 a // b
# 取余 a % b
# 幂运算 a ** b

# 请在这里写下你的代码
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} %  {b} = {a % b}")
print(f"{a} ** {b} = {a ** b}")

# 2. 面积计算
# 已知圆的半径r = 5，计算圆的面积和周长
# 面积公式：π * r²
# 周长公式：2 * π * r
# π可以取3.14159

r = 5
pi = 3.14159

# 计算面积area和周长perimeter
# 请在这里写下你的代码
area = pi * r * r
perimeter = 2 * pi * r

print(f"半径为{r}的圆：")
print(f"面积 = {area:.2f}")
print(f"周长 = {perimeter:.2f}")

# 3. 温度转换
# 将摄氏温度25度转换为华氏温度
# 公式：F = C * 9/5 + 32

celsius = 25
# 计算华氏温度fahrenheit
# 请在这里写下你的代码
fahrenheit = (celsius * 9 / 5) + 32

print(f"{celsius}摄氏度 = {fahrenheit}华氏度")
