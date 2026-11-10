# `dict.setdefault()` — 字典方法

> **功能：** 键存在时直接取原值；不存在时插入默认值并返回。

<a href="../../../../tools/containers.html#dict.setdefault">在交互式图鉴中查看这个方法的操作图解</a>

## 调用形式

```python
d.setdefault(key, default=None)
```

## 参数说明

- **`key`**（可哈希对象）：查找或插入的键。
- **`default`**（任意对象；默认 None）：只有键不存在时才作为新值插入。

**返回值：** 现有值；否则为新插入的默认值

**是否修改原容器：** 可能修改：只在键缺失时插入。

## 时间复杂度

**平均 O(1)**

解释：哈希查找，必要时进行插入。

## 可运行示例

```python
d = {"a": 1}
print(d.setdefault("a", 9))
print(d.setdefault("b", 2))
print(d)
```

输出：

```text
1
2
{'a': 1, 'b': 2}
```

## 执行过程

1. 键 a 已存在，直接返回 1，不会覆盖为 9。
2. 键 b 不存在，插入 b→2。
3. 第二次返回的是新插入的 2。

## 常见错误与风险

- 与 get 的根本区别是会在字典里添加缺失的键。
- default 表达式会在调用前求值，即便键已存在；可变默认对象共享问题需注意。

## 参考依据

- [Python 官方文档：Built-in Types（内置类型）](https://docs.python.org/3/library/stdtypes.html)
- [Python Wiki：TimeComplexity（CPython 常见时间复杂度）](https://wiki.python.org/moin/TimeComplexity)
