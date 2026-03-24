# 13-面向对象 - 学习要点

## 核心知识点

### 1. 类和对象
- **类**：是模板，定义属性和方法
- **对象**：是类的实例，根据模板创建出来的具体东西

### 2. 定义类
```python
class Person:
    # 构造方法：初始化对象属性
    def __init__(self, name, age):
        self.name = name  # 给对象的name属性赋值
        self.age = age

    # 定义方法，第一个参数必须是self，表示对象本身
    def say_hello(self):
        print(f"你好，我是{self.name}，今年{self.age}岁")

# 创建对象
p = Person("张三", 18)
p.say_hello()  # 调用方法，不需要传self
```

### 3. 继承
```python
# Student 继承 Person
class Student(Person):
    def __init__(self, name, age, school):
        # 调用父类的__init__
        super().__init__(name, age)
        self.school = school  # 添加自己的属性

    # 重写方法
    def say_hello(self):
        super().say_hello()
        print(f"我在{self.school}上学")
```

## 练习目标
- 掌握类定义
- 掌握`__init__`构造方法
- 理解self
- 会定义方法，创建对象
