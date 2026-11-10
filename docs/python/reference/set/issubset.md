# `set.issubset()` — 集合方法

> **功能：** 检查当前集合的所有元素是否都在 other 中。

<a href="../../../../tools/containers.html#set.issubset">在交互式图鉴中查看这个方法的操作图解</a>

## 调用形式

```python
s.issubset(other)
```

## 参数说明

- **`other`**（集合或可迭代对象）：被判断是否包含当前集合的目标。

**返回值：** bool（True/False）

**是否修改原容器：** 否。

## 时间复杂度

**两个 set 平均 O(|A|)，可提前失败**

解释：逐个检查 A 的成员是否包含于 B；若 B 不是 set，还可能有构建成本。

## 可运行示例

```python
a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))
print(b.issubset(a))
```

输出：

```text
True
False
```

## 执行过程

1. 检查 a 的每个成员：1、2 均在 b 中。
2. 所以 a 是 b 的子集，返回 True。
3. 反向检查 b 时，3 不在 a 中，返回 False。

## 常见错误与风险

- 空集是任意集合的子集。
- A <= B 允许相等；A < B 才是严格真子集。

## 参考依据

- [Python 官方文档：Built-in Types（内置类型）](https://docs.python.org/3/library/stdtypes.html)
- [Python Wiki：TimeComplexity（CPython 常见时间复杂度）](https://wiki.python.org/moin/TimeComplexity)
