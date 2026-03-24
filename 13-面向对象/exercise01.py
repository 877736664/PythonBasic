"""
13-面向对象 - 练习1
练习目标：掌握类定义、__init__、方法
"""

# 1. 定义一个矩形类 Rectangle
# 要求：
# - __init__接收长和宽 width, height
# - 方法 area() 计算面积并返回
# - 方法 perimeter() 计算周长并返回
# 请写下代码

class Rectangle:
    def __init__(self, width, height):
        # 补充代码
        pass

    def area(self):
        # 补充代码
        pass

    def perimeter(self):
        # 补充代码
        pass


# 测试
rect = Rectangle(3, 4)
print(f"长3宽4：面积 = {rect.area()}, 周长 = {rect.perimeter()}")
print("-" * 30)

# 2. 定义一个圆类 Circle
# 要求：
# - __init__接收半径 radius
# - 方法 area() 计算面积
# - 方法 perimeter() 计算周长
# 提示：π 可以用 math.pi
import math

class Circle:
    pass


# 测试
c = Circle(5)
print(f"半径5：面积 = {c.area():.2f}, 周长 = {c.perimeter():.2f}")
print("-" * 30)

# 3. 定义学生类 Student
# 要求：
# - 属性：name姓名，score分数列表
# - __init__接收name，scores是可选参数，默认空列表
# - 方法 add_score(score) 添加一个分数
# - 方法 get_average() 计算平均分返回
# 请写下代码

class Student:
    pass


# 测试
stu = Student("张三")
stu.add_score(85)
stu.add_score(92)
stu.add_score(78)
print(f"{stu.name} 的平均分：{stu.get_average():.2f}")
