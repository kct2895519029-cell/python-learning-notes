# `set.discard()` — 集合方法

> **功能：** 如果目标存在就删除；不存在时不报错。

<a href="../../../../tools/containers.html#set.discard">在交互式图鉴中查看这个方法的操作图解</a>

## 调用形式

```python
s.discard(item)
```

## 参数说明

- **`item`**（待删除元素）：如 2 或 "hello"。

**返回值：** None

**是否修改原容器：** 可能修改。

## 时间复杂度

**平均 O(1)**

解释：哈希查询；存在时执行删除。

## 可运行示例

```python
s = {1, 2}
s.discard(9)
s.discard(2)
print(sorted(s))
```

输出：

```text
[1]
```

## 执行过程

1. 9 不在集合中，不做任何修改。
2. 2 存在，因此被删除。
3. 剩下成员 1。

## 常见错误与风险

- “安全删除”仅指目标缺失时不会抛 KeyError；传入不合适对象仍可能出错。

## 参考依据

- [Python 官方文档：Built-in Types（内置类型）](https://docs.python.org/3/library/stdtypes.html)
- [Python Wiki：TimeComplexity（CPython 常见时间复杂度）](https://wiki.python.org/moin/TimeComplexity)
