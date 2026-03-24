"""
03-流程控制 - 练习1
练习目标：掌握if条件判断
"""

# 1. 判断成绩等级
score = int(input("请输入成绩(0-100)："))

# 判断规则：
# 90分以上：优秀
# 80-89分：良好
# 70-79分：中等
# 60-69分：及格
# 60分以下：不及格
# 请在这里写下你的代码
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 70:
    print("中等")
elif score >= 60:
    print("及格")
else:
    print("不及格")


# 2. 判断一个数是正数、负数还是零
num = float(input("请输入一个数字："))

# 请在这里写下你的代码
if  num > 0:
    print("正数")
elif num < 0 :
    print("负数")
else:
    print("零")

# 3. 判断 BMI 指数
# BMI = 体重(kg) / (身高(m)²)
# 分类：
# BMI < 18.5：偏瘦
# 18.5 <= BMI < 24：正常
# 24 <= BMI < 28：偏胖
# BMI >= 28：肥胖

weight = float(input("请输入体重(kg)："))
height = float(input("请输入身高(m)："))

# 计算BMI并判断分类
# 请在这里写下你的代码
BMI = weight / (height * height)

if BMI < 18.5:
    print("偏瘦")
elif BMI < 24:
    print("正常")
elif BMI < 28:
    print("偏胖")
else:
    print("肥胖")
