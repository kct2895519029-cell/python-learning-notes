# `set.symmetric_difference()` — 集合方法

> **功能：** 计算对称差集：仅出现于其中一个集合的成员。

<a href="../../../../tools/containers.html#set.symmetric_difference">在交互式图鉴中查看这个方法的操作图解</a>

## 调用形式

```python
s.symmetric_difference(other)
```

## 参数说明

- **`other`**（一个可迭代对象）：与当前集合比较成员差异。

**返回值：** 新的 set 集合

**是否修改原容器：** 否。

## 时间复杂度

**两个 set 平均 O(|A|+|B|)**

解释：复制一边并依据另一边的成员进行翻转/增删。

## 可运行示例

```python
a = {1, 2, 3}
b = {2, 4}
print(sorted(a.symmetric_difference(b)))
```

输出：

```text
[1, 3, 4]
```

## 执行过程

1. 成员 2 两边都有，因此被排除。
2. 成员 1、3 只在 A 中，成员 4 只在 B 中。
3. 结果为 1、3、4。

## 常见错误与风险

- 等价于 (A-B) ∪ (B-A)，不等于普通差集。
- 方法仅接收一个 other，而非多个其他对象。

## 参考依据

- [Python 官方文档：Built-in Types（内置类型）](https://docs.python.org/3/library/stdtypes.html)
- [Python Wiki：TimeComplexity（CPython 常见时间复杂度）](https://wiki.python.org/moin/TimeComplexity)
