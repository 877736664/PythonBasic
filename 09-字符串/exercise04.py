"""
09-字符串 - 练习4
练习目标：掌握字符串判断方法
"""

# 判断练习
# 判断字符串 "12345" 是否全是数字
# 判断 "https://" 是否以 "http" 开头
# 判断 "test.py" 是否以 ".py" 结尾
# 请写下代码

num_str = "12345"
is_all_digit = num_str.isdigit()
print(f"{num_str} 全是数字吗？{is_all_digit}")

url = "https://"
start_with_http = url.startswith("http")
print(f"{url} 以http开头吗？{start_with_http}")

filename = "test.py"
end_with_py = filename.endswith(".py")
print(f"{filename} 以.py结尾吗？{end_with_py}")
