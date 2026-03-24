"""
04-函数 - 练习2
练习目标：掌握参数默认值、可变参数、返回值
"""

# 1. 定义一个函数，可以计算多个数的平均值
def average(*numbers):
    # numbers接收任意多个参数
    # 计算平均值并返回
    # 如果没有参数，返回0
    # 请在这里补充代码
    if len(numbers) == 0:
        return 0
    return sum(numbers)/len(numbers)

# 测试
print(f"average(1, 2, 3, 4, 5) = {average(1, 2, 3, 4, 5)}")
print(f"average(10, 20) = {average(10, 20)}")
print(f"average() = {average()}")

# 2. 定义一个函数，返回多个值：计算一个列表的最大值和最小值
def find_max_min(numbers):
    # 返回 (最大值, 最小值)
    # 请在这里补充代码
    if len(numbers) == 0:
        return (0, 0)
    return max(numbers), min(numbers)

# 测试
nums = [3, 1, 4, 1, 5, 9, 2, 6]
max_val, min_val = find_max_min(nums)
print(f"最大值：{max_val}, 最小值：{min_val}")

# 3. 递归练习：计算阶乘 n! = n * (n-1) * ... * 1
def factorial(n):
    # 请在这里补充代码（递归实现）
    # ========== 解题思路 ==========
    # 递归 = 基线条件 + 递归关系
    # 基线条件：递归停止的条件，题目说 0! = 1，所以 n <= 1 都返回 1
    # 递归关系：n! = n × (n-1)!，自己调用自己计算更小的子问题
    # 例如：5! = 5 × 4! → 4! = 4 × 3! → 3! = 3 × 2! → 2! = 2 × 1! → 1! = 1
    # 然后层层返回结果：1 → 2×1=2 → 3×2=6 → 4×6=24 → 5×24=120
    if n <= 1:  # 基线条件
        return 1
    return n * factorial(n - 1)  # 递归调用


# 测试
print(f"factorial(5) = {factorial(5)}")  # 应该是120
print(f"factorial(0) = {factorial(0)}")  # 0! = 1

# 4. 递归练习：斐波那契数列第n项
# F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2)
def fibonacci(n):
    # 请在这里补充代码
    # ========== 解题思路 ==========
    # 递归模式和上面一样，题目已经把规则给我们了：
    # 基线条件：F(0) = 0, F(1) = 1
    # 递归关系：F(n) = F(n-1) + F(n-2)
    # 直接按照题目给的公式写出来就行
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# 测试
print(f"fibonacci(0) = {fibonacci(0)}")
print(f"fibonacci(1) = {fibonacci(1)}")
print(f"fibonacci(5) = {fibonacci(5)}")
print(f"fibonacci(10) = {fibonacci(10)}")
