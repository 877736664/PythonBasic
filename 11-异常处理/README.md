# 11-异常处理 - 学习要点

## 核心知识点

### 1. 为什么需要异常处理
当程序可能出错时，提前捕获错误，不让程序崩溃

### 2. 基本语法
```python
try:
    # 可能出错的代码
    num = int(input("请输入数字："))
except ValueError:
    # 捕获ValueError错误
    print("输入不是有效的整数")
except (TypeError, ZeroDivisionError):
    # 捕获多种错误
else:
    # 没有出错才执行
    print("输入正确")
finally:
    # 不管有没有错都会执行，用于清理资源
    print("结束")
```

### 3. 常见异常
| 异常 | 原因 |
|------|------|
| `ValueError` | 值错误，比如类型转换失败 |
| `IndexError` | 索引越界 |
| `KeyError` | 字典key不存在 |
| `ZeroDivisionError` | 除零错误 |
| `FileNotFoundError` | 文件不存在 |
| `TypeError` | 类型错误，参数不对 |

## 练习目标
- 掌握 try-except 语法
- 能捕获常见异常
