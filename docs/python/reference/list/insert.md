# `list.insert()` — 列表方法

> **功能：** 把元素插入指定位置，后面的元素向右移动。

<a href="../../../../tools/containers.html#list.insert">在交互式图鉴中查看这个方法的操作图解</a>

## 调用形式

```python
a.insert(index, item)
```

## 参数说明

- **`index`**（整数索引）：插入到该索引所指元素之前；负索引从后往前定位。
- **`item`**（任意对象）：要插入的单个对象。

**返回值：** None

**是否修改原容器：** 是。

## 时间复杂度

**O(n)，头部最贵**

解释：插入位置后方约有 n-index 个元素需要移动。

## 可运行示例

```python
a = [10, 30]
a.insert(1, 20)
print(a)
a.insert(999, 40)
print(a)
```

输出：

```text
[10, 20, 30]
[10, 20, 30, 40]
```

## 执行过程

1. 先把 20 插到索引 1（原 30 之前）。
2. 后面的元素整体右移。
3. 索引 999 超出末尾，插到尾部。

## 常见错误与风险

- index 大于长度时放在尾部；负值过小时放在头部，不抛出越界错误。
- 频繁头插可考虑 collections.deque 的 appendleft。

## 参考依据

- [Python 官方文档：Built-in Types（内置类型）](https://docs.python.org/3/library/stdtypes.html)
- [Python Wiki：TimeComplexity（CPython 常见时间复杂度）](https://wiki.python.org/moin/TimeComplexity)
