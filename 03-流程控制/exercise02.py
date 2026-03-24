"""
03-流程控制 - 练习2
练习目标：掌握for循环和while循环
"""

# 1. 打印1-100之间所有的偶数
# 使用for循环
print("1-100之间的偶数：")
# 请在这里写下你的代码
for i in range(2, 101, 2):
    print(i)


# 2. 计算1-100的累加和
total = 0
# 使用while循环
# 请在这里写下你的代码
i = 1
while i <= 100 :
    total = total + i
    i = i + 1

print(f"1-100的累加和：{total}")

# 3. 打印九九乘法表
# 提示：使用嵌套循环
# 请在这里写下你的代码
for i in range(1, 10):          # i 表示第几行，共9行
    for j in range(1, i + 1):   # j 表示第几列，第i行有i个式子
        # 打印每个乘法式子，end="" 表示不换行，\t用于对齐
        print(f"{i}*{j} = {i * j}")
    print()

# 4. 猜数字游戏
# 生成一个1-100之间的随机数，让用户猜
import random
secret = random.randint(1, 100)
count = 0

print("欢迎来到猜数字游戏！数字在1-100之间")
# 循环让用户猜，直到猜对为止
# 提示太大了或太小了
# 请在这里写下你的代码
while True:
    guess = int(input("请输入你猜的数字: "))
    count += 1
    if guess > secret:
        print("太大了")
    elif guess < secret:
        print("太小了")
    else:
        print(f"恭喜你猜对了！答案就是{secret}")
        print(f"你一共猜了{count}次")
        break