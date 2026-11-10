# `set.add()` — 集合方法

> **功能：** 向集合中添加一个可哈希的元素，若已存在则不重复添加。

<a href="../../../../tools/containers.html#set.add">在交互式图鉴中查看这个方法的操作图解</a>

## 调用形式

```python
s.add(item)
```

## 参数说明

- **`item`**（可哈希对象）：如整数、字符串、符合要求的元组；普通 list/dict/set 不可直接加入。

**返回值：** None

**是否修改原容器：** 可能修改：仅元素尚不存在时增加。

## 时间复杂度

**平均 O(1)**

解释：哈希定位和插入；冲突严重时变慢。

## 可运行示例

```python
s = {1, 2}
s.add(3)
s.add(2)
print(sorted(s))
```

输出：

```text
[1, 2, 3]
```

## 执行过程

1. 集合最初包含 1、2。
2. add(3) 新增一个元素。
3. add(2) 不会产生第二个 2。

## 常见错误与风险

- 不能 add([1,2])：普通列表不可哈希，抛 TypeError。
- 集合中的相等元素合并，如 1 与 True 通常视为相等。

## 参考依据

- [Python 官方文档：Built-in Types（内置类型）](https://docs.python.org/3/library/stdtypes.html)
- [Python Wiki：TimeComplexity（CPython 常见时间复杂度）](https://wiki.python.org/moin/TimeComplexity)
