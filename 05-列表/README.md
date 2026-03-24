# 05-列表 - 学习要点

## 核心知识点

### 1. 什么是列表
- 列表是**有序可变**的容器，可以存放任意类型的数据
- 用方括号 `[]` 表示，元素用逗号分隔
```python
empty = []                # 空列表
nums = [1, 2, 3, 4]      # 整数列表
mixed = [1, "hello", True, None]  # 不同类型可以混放
```

### 2. 索引访问
- 索引从 `0` 开始
- 支持负索引：`-1` 是最后一个，`-2` 是倒数第二个
```python
lst = [a, b, c, d]
# 索引:  0  1  2  3
# 负索引: -4 -3 -2 -1

print(lst[0])   # 第一个元素
print(lst[-1])  # 最后一个元素
```

### 3. 切片操作
```python
lst[start:stop:step]
```
- 包含 `start`，不包含 `stop`
- `start` 省略从头开始，`stop` 省略到末尾
```python
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
nums[:3]      # [0, 1, 2]      前三个
nums[2:6]     # [2, 3, 4, 5]
nums[::2]     # [0, 2, 4, 6, 8] 步长2
nums[::-1]    # 反转整个列表
```

### 4. 常用方法（增删改查）

**增加元素：**
| 方法 | 作用 |
|------|------|
| `append(x)` | 在末尾添加一个元素 |
| `insert(i, x)` | 在索引i位置插入x |
| `extend(iterable)` | 在末尾添加多个元素 |

**删除元素：**
| 方法 | 作用 |
|------|------|
| `pop()` | 删除并返回最后一个元素 |
| `pop(i)` | 删除并返回索引i位置的元素 |
| `remove(x)` | 删除第一个值为x的元素 |
| `clear()` | 清空整个列表 |

**查找：**
| 方法 | 作用 |
|------|------|
| `index(x)` | 返回第一个x的索引，找不到报错 |
| `count(x)` | 返回x出现的次数 |

**排序：**
| 方法 | 作用 |
|------|------|
| `sort()` | 原地升序排序 |
| `sort(reverse=True)` | 原地降序排序 |
| `sorted(lst)` | 返回新的排序后的列表，原列表不变 |

**其他：**
- `len(lst)` - 获取长度（内置函数，不是方法）
- `reverse()` - 原地反转

### 5. 列表推导式（List Comprehension）
简洁生成列表的语法：
```python
# 生成1-10的平方
squares = [x**2 for x in range(1, 11)]

# 带条件：只保留偶数
evens = [x for x in range(1, 21) if x % 2 == 0]
```

### 6. 去重方法
```python
# 方法1：用set转换（简单，无序）
lst = [1, 2, 2, 3, 3, 3]
unique = list(set(lst))

# 方法2：保持顺序遍历去重
unique = []
for x in lst:
    if x not in unique:
        unique.append(x)
```

### 7. 遍历列表
```python
# 直接遍历元素
for item in lst:
    print(item)

# 需要索引时用enumerate
for i, item in enumerate(lst):
    print(i, item)
```

## 练习目标
- ✓ 掌握索引和切片操作
- ✓ 掌握增删改查常用方法
- ✓ 掌握排序
- ✓ 理解并会用列表推导式
- ✓ 能解决简单问题：去重、找最大最小、合并排序等
