"""
11-异常处理 - 练习1
练习目标：掌握try-except捕获异常
"""

# 1. 安全的整数转换
# 写一个函数，尝试把输入转成整数，如果失败返回 None
def to_int(s):
    # 请用try-except实现

    pass

# 测试
print(f"to_int('123') = {to_int('123')}")   # 应该是123
print(f"to_int('abc') = {to_int('abc')}")   # 应该是None
print("-" * 30)

# 2. 安全的除法
# 输入两个数，计算 a / b，如果b是0返回None
def safe_divide(a, b):
    # 请实现



# 测试
print(f"safe_divide(10, 2) = {safe_divide(10, 2)}")  # 5.0
print(f"safe_divide(8, 0) = {safe_divide(8, 0)}")    # None
print("-" * 30)

# 3. 安全获取列表元素
# 根据索引获取列表元素，如果索引越界返回None
def get_element(lst, index):
    # 请实现


    pass

# 测试
nums = [1, 2, 3, 4, 5]
print(f"get_element(nums, 2) = {get_element(nums, 2)}")  # 3
print(f"get_element(nums, 10) = {get_element(nums, 10)}") # None
