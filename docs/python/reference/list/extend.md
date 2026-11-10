# `list.extend()` — 列表方法

> **功能：** 遍历可迭代对象，把其中元素逐个添加到列表末尾。

<a href="../../../../tools/containers.html#list.extend">在交互式图鉴中查看这个方法的操作图解</a>

## 调用形式

```python
a.extend(iterable)
```

## 参数说明

- **`iterable`**（可迭代对象）：如列表、元组、字符串、生成器；每次迭代取一个元素。

**返回值：** None

**是否修改原容器：** 是：原列表被扩展。

## 时间复杂度

**O(k)，k 为实际追加的元素数**

解释：需要逐个取得并放入 k 个元素；扩容成本均摊。

## 可运行示例

```python
a = [1, 2]
a.extend([3, 4])
print(a)
a.extend("AB")
print(a)
```

输出：

```text
[1, 2, 3, 4]
[1, 2, 3, 4, 'A', 'B']
```

## 执行过程

1. 原列表为 [1, 2]。
2. extend([3, 4]) 逐一追加 3 和 4。
3. 字符串也可迭代，因此 "AB" 被分成两个字符。

## 常见错误与风险

- extend("ab") 添加的是 "a" 和 "b" 两个字符。
- 不能传入不可迭代的整数，如 extend(3)。

## 参考依据

- [Python 官方文档：Built-in Types（内置类型）](https://docs.python.org/3/library/stdtypes.html)
- [Python Wiki：TimeComplexity（CPython 常见时间复杂度）](https://wiki.python.org/moin/TimeComplexity)
