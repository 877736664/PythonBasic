"""
07-字典 - 练习1
练习目标：掌握字典增删改查基本操作
"""

# 1. 创建字典
# 请创建一个学生字典，包含：
# name: 张三
# age: 20
# score: 85.5
# hobbies: ["篮球", "编程"]
# 变量名 student
# 请写下代码

student = {
    "name": "张三",
    "age": 20,
    "score": 85.5,
    "hobbies": ["篮球", "编程"],
}

print(f"学生信息：{student}")
print(f"姓名：{student['name']}")
print(f"爱好：{student['hobbies']}")
print("-" * 30)

# 2. 修改和添加
# 请完成：
# - 年龄改为 21
# - 添加一个键 grade，值是 "大三"
# 请写下代码
student["age"] = 21
student["grade"] = "大三"

print(f"修改后：{student}")
print("-" * 30)

# 3. 查找
# 用 get 方法获取 score，如果不存在返回 0
# 请写下代码

score = student.get("score")

print(f"分数：{score}")

# 获取一个不存在的键 gender，默认值 "未知"
gender = student.get("gender", "未知")
print(f"性别：{gender}")
print("-" * 30)

# 4. 删除
# 删除键 hobbys 删错了，应该是 hobbies
# 请删除 hobbies
# 请写下代码
student.pop("hobbies")


print(f"删除hobbies后：{student}")
print("-" * 30)

# 5. 遍历字典
# 遍历 student，打印所有 "键: 值"
# 格式：name: 张三，age: 21...
# 请写下代码
for key, value in student.items():
    print(f"{key}: {value}")
