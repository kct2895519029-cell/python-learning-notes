# `dict.update()` — 字典方法

> **功能：** 批量新增键值对或覆盖已有键对应的值。

<a href="../../../../tools/containers.html#dict.update">在交互式图鉴中查看这个方法的操作图解</a>

## 调用形式

```python
d.update(other, **kwargs)
```

## 参数说明

- **`other`**（映射或二元组可迭代对象，可选）：例如 {"a": 2} 或 [("a", 2)]。
- **`**kwargs`**（关键字参数，可选）：例如 d.update(city="Yibin")，键名作为字符串。

**返回值：** None

**是否修改原容器：** 是。

## 时间复杂度

**O(k)，k 为输入的键值对数（均摊）**

解释：需逐项执行哈希写入，散列表偶尔扩容。

## 可运行示例

```python
d = {"a": 1}
d.update({"a": 9, "b": 2})
print(d)
```

输出：

```text
{'a': 9, 'b': 2}
```

## 执行过程

1. 输入有两个键值对：a→9 与 b→2。
2. a 已存在，原值 1 被覆盖。
3. b 不存在，新增键值对。

## 常见错误与风险

- 同名键会静默覆盖旧值。
- update([("x",1)]) 合法；不是所有可迭代对象都可用，元素必须能表示键值对。

## 参考依据

- [Python 官方文档：Built-in Types（内置类型）](https://docs.python.org/3/library/stdtypes.html)
- [Python Wiki：TimeComplexity（CPython 常见时间复杂度）](https://wiki.python.org/moin/TimeComplexity)
