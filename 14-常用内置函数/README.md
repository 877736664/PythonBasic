# 14-常用内置函数 - 学习要点

## 常用内置函数总结

### 1. 类型相关
| 函数 | 作用 |
|------|------|
| `type(x)` | 获取x的类型 |
| `isinstance(x, type)` | 判断x是否是某种类型 |
| `int(x)` / `float(x)` / `str(x)` | 类型转换 |

### 2. 数学相关
| 函数 | 作用 |
|------|------|
| `abs(x)` | 绝对值 |
| `round(x, n)` | 四舍五入，保留n位小数 |
| `max(iterable)` / `min(iterable)` | 最大最小值 |
| `sum(iterable)` | 求和 |
| `len(iterable)` | 获取长度 |
| `pow(a, b)` | a的b次方 |

### 3. 序列相关
| 函数 | 作用 |
|------|------|
| `range(start, stop, step)` | 生成整数序列 |
| `sorted(iterable, reverse=False)` | 排序，返回新列表 |
| `reversed(seq)` | 反转，返回迭代器 |
| `enumerate(seq)` | 返回 (索引, 值) 对，常用于循环 |
| `zip(a, b)` | 把两个序列打包成元组迭代 |

### 4. 其他
| 函数 | 作用 |
|------|------|
| `map(func, iterable)` | 对每个元素应用函数，返回迭代器 |
| `filter(func, iterable)` | 过滤，保留func返回True的元素 |
| `any(iterable)` | 有一个True就返回True |
| `all(iterable)` | 全部True才返回True |

## 练习目标
- 掌握常用内置函数的用法
- 会灵活运用解决问题
