# 题目 2：判断正数、负数、零
# 输入一个整数 n：
#
# 如果 n > 0，输出 "positive"
# 如果 n < 0，输出 "negative"
# 如果 n == 0，输出 "zero"

n = int(input())
if n > 0:
    print("positive")
elif n < 0:
    print("negative")
else:
    print("zero")
