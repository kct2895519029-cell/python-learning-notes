# `set.intersection()` — 集合方法

> **功能：** 计算交集：只保留同时存在于所有输入中的元素。

<a href="../../../../tools/containers.html#set.intersection">在交互式图鉴中查看这个方法的操作图解</a>

## 调用形式

```python
s.intersection(*others)
```

## 参数说明

- **`*others`**（一个或多个可迭代对象）：与当前集合求共同成员。

**返回值：** 新的 set 集合

**是否修改原容器：** 否。

## 时间复杂度

**两个 set 平均 O(min(|A|,|B|))**

解释：对较小集合逐个成员检查；非 set 可迭代对象时复杂度取决于转换与长度。

## 可运行示例

```python
a = {1, 2}
b = {2, 3}
print(sorted(a.intersection(b)))
print(sorted(a))
```

输出：

```text
[2]
[1, 2]
```

## 执行过程

1. 比较 a 和 b。
2. 只有元素 2 同时出现在两边。
3. 返回 {2}，原 a 不变。

## 常见错误与风险

- s.intersection([2,3]) 合法；s & [2,3] 通常抛 TypeError。
- 求交集之后原集合不会改变。

## 参考依据

- [Python 官方文档：Built-in Types（内置类型）](https://docs.python.org/3/library/stdtypes.html)
- [Python Wiki：TimeComplexity（CPython 常见时间复杂度）](https://wiki.python.org/moin/TimeComplexity)
