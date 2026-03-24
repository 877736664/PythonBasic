"""
06-元组 - 练习2
练习目标：掌握元组和列表转换、函数多返回值、交换变量
"""

# 1. 列表和元组转换
# 把列表 [1, 2, 3, 4, 5] 转成元组
# 再把元组转成列表
lst = [1, 2, 3, 4, 5]
# 请补充代码

t = tuple(lst)
print(f"转成元组：{t}, 类型是 {type(t)}")

new_lst = list(t)
print(f"转回列表：{new_lst}, 类型是 {type(new_lst)}")
print("-" * 30)

# 2. 函数返回多个值（其实就是返回元组）
# 定义一个函数 divide(a, b)
# 返回 (商, 余数)
# 例如 divide(10, 3) → (3, 1)
# 请写下代码

def divide(a, b):
    # 计算商和余数，返回
    shang = a // b
    yushu = a % b
    return shang, yushu


# 测试
q, r = divide(10, 3)
print(f"10 ÷ 3 = 商 {q}, 余数 {r}")
print("-" * 30)

# 3. 使用元组解包交换两个变量
# 不用临时变量，交换 a 和 b 的值
a = 10
b = 20
print(f"交换前：a={a}, b={b}")

# 请在这里写下交换代码
a, b = b, a

print(f"交换后：a={a}, b={b}")
print("-" * 30)

# 4. 统计元组中某个元素出现的次数
t = (1, 2, 2, 3, 3, 3, 4, 4, 5)
# 统计 3 出现几次，结果存在 count_three
# 提示：元组也有 count() 方法，和列表一样

count_three = t.count(3)
print(f"3在元组中出现了 {count_three} 次")

# 判断 5 是否在元组中，结果存在 has_five
has_five = 5 in t
print(f"元组中包含5吗？{has_five}")
