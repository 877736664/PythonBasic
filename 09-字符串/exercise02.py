"""
09-字符串 - 练习2
练习目标：掌握字符串常用方法
"""

# 字符串方法练习
text = "  hello world! hello python!  "

# 请：
# 1. 去除两端空白
# 2. 统计hello出现次数
# 3. 把所有空格替换成-
# 4. 按空格分割成单词列表
# 请写下代码

text_stripped = text.strip()
print(f"去除空白后：'{text_stripped}'")

count_hello = text.count("hello")
print(f"hello出现次数：{count_hello}")

text_replaced = text.replace(" ", "-")
print(f"替换空格：{text_replaced}")

words = text.split()
print(f"分割后：{words}")
