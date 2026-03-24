"""
09-字符串 - 练习1
练习目标：掌握字符串切片
"""

# 切片练习
s = "Hello,Python!"

# 请：
# 1. 获取前5个字符
# 2. 获取从索引7到末尾
# 3. 获取每个单词的首字母（索引0和索引6）
# 4. 反转整个字符串
# 请写下代码

first5 = s[:5]
print(f"前5个字符：{first5}")

from7 = s[7:]
print(f"索引7到末尾：{from7}")

first_letter1 = s[0]
first_letter2 = s[6]
print(f"首字母：{first_letter1}, {first_letter2}")

reversed_s = s[::-1]
print(f"反转后：{reversed_s}")
