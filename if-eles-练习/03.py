# 输入一个整数 score（0~100）：
#
# 90~100：输出 "A"
# 80~89：输出 "B"
# 70~79：输出 "C"
# 60~69：输出 "D"
# 0~59：输出 "E"
# 如果分数小于 0 或大于 100，输出 "invalid score"

score = int(input())
if score < 0 or score > 100:
    print("invalid score")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("E")