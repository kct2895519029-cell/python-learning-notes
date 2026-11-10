# `list.copy()` — 列表方法

> **功能：** 创建一个新列表，但内部元素的引用只复制一层。

<a href="../../../../tools/containers.html#list.copy">在交互式图鉴中查看这个方法的操作图解</a>

## 调用形式

```python
b = a.copy()
```

## 参数说明

本方法不需要额外参数。

**返回值：** 新列表对象

**是否修改原容器：** 否：a 未改动（但随后修改共享子对象会互相可见）。

## 时间复杂度

**O(n)**

解释：必须复制 n 个元素槽位及其对象引用。

## 可运行示例

```python
a = [[1], [2]]
b = a.copy()
b[0].append(9)
print(a)
print(b)
print(a is b)
```

输出：

```text
[[1, 9], [2]]
[[1, 9], [2]]
False
```

## 执行过程

1. b 是新建的外层列表，所以 a is b 为 False。
2. b[0] 与 a[0] 仍指向同一个子列表。
3. 对子列表追加 9，两边都能观察到。

## 常见错误与风险

- 浅拷贝不复制嵌套列表、字典。
- b[0].append(...) 会改变两份列表共享的内部列表。
- 若需要深层独立，请研究 copy.deepcopy。

## 参考依据

- [Python 官方文档：Built-in Types（内置类型）](https://docs.python.org/3/library/stdtypes.html)
- [Python Wiki：TimeComplexity（CPython 常见时间复杂度）](https://wiki.python.org/moin/TimeComplexity)
