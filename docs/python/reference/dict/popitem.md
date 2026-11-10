# `dict.popitem()` — 字典方法

> **功能：** 删除并返回最后插入的键值对（Python 3.7+ 保证后进先出）。

<a href="../../../../tools/containers.html#dict.popitem">在交互式图鉴中查看这个方法的操作图解</a>

## 调用形式

```python
d.popitem()
```

## 参数说明

本方法不需要额外参数。

**返回值：** (key, value) 二元组

**是否修改原容器：** 是。

## 时间复杂度

**平均 O(1)**

解释：在保持插入顺序的字典中移除末项。

## 可运行示例

```python
d = {"a": 1, "b": 2}
item = d.popitem()
print(item)
print(d)
```

输出：

```text
('b', 2)
{'a': 1}
```

## 执行过程

1. a 先插入、b 后插入。
2. popitem() 删除最后插入的 b。
3. 返回 ("b", 2)，字典只剩 a。

## 常见错误与风险

- 空字典会抛 KeyError。
- 修改已有键的值通常不会让它变成“最后插入”的键。

## 参考依据

- [Python 官方文档：Built-in Types（内置类型）](https://docs.python.org/3/library/stdtypes.html)
- [Python Wiki：TimeComplexity（CPython 常见时间复杂度）](https://wiki.python.org/moin/TimeComplexity)
