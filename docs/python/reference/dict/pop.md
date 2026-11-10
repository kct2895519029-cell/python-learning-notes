# `dict.pop()` — 字典方法

> **功能：** 按键删除字典中的一项，并返回对应的值。

<a href="../../../../tools/containers.html#dict.pop">在交互式图鉴中查看这个方法的操作图解</a>

## 调用形式

```python
d.pop(key, default=未提供)
```

## 参数说明

- **`key`**（可哈希对象）：待删除的键。
- **`default`**（任意对象，可选）：键不存在时返回它；若未提供则抛 KeyError。

**返回值：** 删除的值；或 default

**是否修改原容器：** 是。

## 时间复杂度

**平均 O(1)**

解释：按哈希定位键值对。

## 可运行示例

```python
d = {"a": 1, "b": 2}
x = d.pop("a")
print(x)
print(d)
print(d.pop("z", "无此键"))
```

输出：

```text
1
{'b': 2}
无此键
```

## 执行过程

1. 键 a 存在：删除 a 并返回值 1。
2. 原字典只剩 b 对应 2。
3. 键 z 不存在：返回默认字符串，不报错。

## 常见错误与风险

- 未提供 default 且键不存在，会抛 KeyError。
- 注意与 list.pop(索引) 的语义区别。

## 参考依据

- [Python 官方文档：Built-in Types（内置类型）](https://docs.python.org/3/library/stdtypes.html)
- [Python Wiki：TimeComplexity（CPython 常见时间复杂度）](https://wiki.python.org/moin/TimeComplexity)
