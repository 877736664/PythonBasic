# 03-流程控制 - 学习要点

## 核心知识点

### 1. if 条件语句

**基本结构：**
```python
if 条件1:
    代码块1
elif 条件2:
    代码块2
else:
    代码块3
```

**要点：**
- 条件后面必须有冒号 `:`
- 代码块通过**缩进**区分，一般用4个空格
- `elif` = else if，多分支判断
- `else` 是可选的，默认情况

### 2. for 循环

**遍历可迭代对象：**
```python
for 变量 in 可迭代对象:
    循环体
```

**常见用法：**
```python
# 遍历范围 0 ~ 9
for i in range(10):
    print(i)

# 遍历范围 1 ~ 10
for i in range(1, 11):
    print(i)

# 步长为2
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8
```

- `range(start, stop, step)` - 不包含 stop

### 3. while 循环

**结构：**
```python
while 条件:
    循环体
```

- 只要条件为 `True`，就一直循环
- 注意不要写出**死循环**（条件永远为True）

### 4. 循环控制
- `break` - 立即跳出整个循环
- `continue` - 跳过本次循环，开始下一次

**示例：**
```python
for i in range(10):
    if i == 5:
        break      # i=5时直接结束循环
    print(i)        # 输出 0 1 2 3 4

for i in range(10):
    if i % 2 == 0:
        continue   # 偶数跳过，不打印
    print(i)       # 输出 1 3 5 7 9
```

### 5. 嵌套循环
- 循环里面可以再套循环
- 比如九九乘法表就是典型的双层循环

## 常用算法模式

### 累加
```python
total = 0
for i in range(1, 101):
    total += i  # total = total + i
```

### 计数
```python
count = 0
for ...:
    if 符合条件:
        count += 1
```

## 练习目标
- ✓ 掌握if多分支条件判断
- ✓ 掌握for循环和range()用法
- ✓ 掌握while循环
- ✓ 理解break和continue区别
- ✓ 能写出九九乘法表
- ✓ 能写简单的猜数字游戏
