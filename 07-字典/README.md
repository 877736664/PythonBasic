# 07-字典 - 学习要点

## 核心知识点

### 1. 什么是字典
- 字典是**键值对**的无序可变容器
- 键key必须是**不可变类型**（字符串、数字、元组），且唯一
- 值value可以是任意类型
- 用大括号 `{key: value}` 表示

```python
# 创建字典
empty = {}
person = {
    "name": "张三",
    "age": 18,
    "city": "北京"
}
```

### 2. 基本操作

| 操作 | 写法 | 说明 |
|------|------|------|
| 访问 | `d[key]` 或 `d.get(key, 默认)` | `get` 找不到key返回默认不报错 |
| 添加/修改 | `d[key] = value` | key存在则修改，不存在则添加 |
| 删除 | `del d[key]` / `d.pop(key)` | 删除指定key |
| 清空 | `d.clear()` | 清空字典 |
| 判断key存在 | `key in d` | 返回True/False |
| 获取所有key | `d.keys()` |
| 获取所有value | `d.values()` |
| 获取所有键值对 | `d.items()` | 用于 `for k, v in d.items()` 遍历 |

### 3. 遍历字典
```python
# 遍历key
for key in d:
    print(key)

# 遍历键值对
for k, v in d.items():
    print(k, v)
```

## 练习目标
- 掌握字典创建
- 掌握增删改查操作
- 掌握遍历方法
