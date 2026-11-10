# Python 容器核心概念

## 1. 容器是什么

**容器（container）** 是可以存放其他对象的对象。四种内置容器并不相同：

| 类型 | 通俗理解 | 有序/索引 | 可原地增删改 | 常见用途 |
|---|---|---|---|---|
| `list` 列表 | 可改变的顺序清单 | 有序，可按数字索引 | 是 | 处理记录序列 |
| `dict` 字典 | 根据“键”找“值”的表 | 保留插入顺序，按键访问 | 是 | JSON 数据、配置与字段 |
| `tuple` 元组 | 固定长度的有序清单 | 有序，可按数字索引 | 不可替换成员引用 | 固定结构的数据 |
| `set` 集合 | 去重的成员名单 | 不承诺有序，不支持下标 | 是 | 去重、交并差与成员判断 |

!!! note "有序并不等于可以按索引访问"
    `dict` 记住插入次序，但使用 `d["id"]` 按键读取；`list` 使用 `a[0]` 按下标访问。

## 2. 键（key）是什么

字典中 **键** 是用于定位信息的标识，**值** 是与之关联的数据。

```python
ticket = {"id": 101, "title": "登录失败"}
print(ticket["title"])  # 输出：登录失败
```

`"title"` 是键，相当于 Excel 表格里的列名；`"登录失败"` 是值；`ticket["title"]` 表示按该字段名取值。

## 3. 可迭代对象（iterable）是什么

**可迭代对象** 是可以被 `for` 循环逐项读取的对象。

```python
for ch in "ABC":
    print(ch)
# A
# B
# C
```

字符串、列表、元组、集合和字典都可迭代，但字典默认迭代的是**键**。

## 4. 视图对象（view）是什么

`d.keys()`、`d.values()` 和 `d.items()` 返回的是一种动态“观察窗口”，不是立即复制出来的独立列表。

```python
d = {"x": 1}
keys_view = d.keys()
d["y"] = 2
print(list(keys_view))   # ['x', 'y']
```

注意：`list(keys_view)` 才会构造新的列表快照。

## 5. 可哈希（hashable）是什么意思

**可哈希** 通常指对象的哈希值在其生命周期内稳定，并支持与之相符的相等比较；字典键和集合成员必须满足该条件。不能简单理解为“只有不可变对象才可哈希”。

```python
d = {"name": "Python"}  # 字符串可以作为键
# d[[1, 2]] = 3        # TypeError: unhashable type: 'list'
```

## 6. 浅拷贝为什么容易出错

**浅拷贝（shallow copy）** 只复制最外层容器，里面的对象引用可能仍然指向同一对象。

```python
a = [[1], [2]]
b = a.copy()
b[0].append(9)
print(a)  # [[1, 9], [2]]
```

`a is b` 为 `False`，但 `a[0] is b[0]` 为 `True`，所以修改内层列表会同时体现于两边。

## 参考资料

- [Python 官方文档：内置类型](https://docs.python.org/3/library/stdtypes.html)
- [Python 官方文档：术语表](https://docs.python.org/3/glossary.html)
