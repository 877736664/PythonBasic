# 12-模块与包 - 学习要点

## 核心知识点

### 1. 什么是模块
- 一个 `.py` 文件就是一个模块
- 可以导入其他模块使用里面的函数、类、变量

### 2. 导入方式
```python
# 方式1：import 模块名
import math
print(math.pi)

# 方式2：from 模块 import 东西
from math import pi, sqrt
print(pi)
print(sqrt(4))

# 方式3：from 模块 import * （不推荐，污染命名空间）
from math import *

# 别名
import numpy as np
from math import pi as π
```

### 3. `__name__` 变量
- 当直接运行模块时，`__name__ == "__main__"`
- 当被导入时，`__name__` 是模块文件名
- 常用写法：
```python
def main():
    # 测试代码
    pass

if __name__ == "__main__":
    main()
```

### 4. 包
- 包就是包含 `__init__.py` 的文件夹，可以包含多个模块
- 导入：`from package.module import func`

## 练习目标
- 掌握导入语法
- 理解 `__name__` 的作用
- 会写自定义模块并导入
