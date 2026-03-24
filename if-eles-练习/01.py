# 题目 1：判断奇偶数
#
# 输入：一个整数 n
# 要求：
# 如果 n 是偶数，输出："even"
# 否则输出："odd"
# 提示：利用整除运算和 if / else 判断

n = int(input())

if n % 2 == 0:
    print("even")
else:
    print("odd")
