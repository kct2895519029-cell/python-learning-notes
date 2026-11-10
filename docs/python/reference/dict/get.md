# `dict.get()` — 字典方法

> **功能：** 按键读取值；键不存在时返回默认值，不抛 KeyError。

<a href="../../../../tools/containers.html#dict.get">在交互式图鉴中查看这个方法的操作图解</a>

## 调用形式

```python
d.get(key, default=None)
```

## 参数说明

- **`key`**（可哈希对象）：要查找的键。
- **`default`**（任意对象；默认 None）：找不到键时直接返回此值；不会写入字典。

**返回值：** 对应的值；不存在则为 default

**是否修改原容器：** 否。

## 时间复杂度

**平均 O(1)**

解释：使用哈希查找；极端冲突或昂贵的 hash/== 可能更慢。

## 可运行示例

```python
d = {"name": "Li"}
print(d.get("name"))
print(d.get("age", 0))
print(d)
```

输出：

```text
Li
0
{'name': 'Li'}
```

## 执行过程

1. 查找 name，发现键存在，得到 Li。
2. 查找 age，键不存在，返回提供的默认值 0。
3. 字典没有出现新键 age。

## 常见错误与风险

- 键存在但对应值为 None，与键不存在但默认 None 无法仅凭结果区分。
- get 不会新增不存在的键。

## 参考依据

- [Python 官方文档：Built-in Types（内置类型）](https://docs.python.org/3/library/stdtypes.html)
- [Python Wiki：TimeComplexity（CPython 常见时间复杂度）](https://wiki.python.org/moin/TimeComplexity)
