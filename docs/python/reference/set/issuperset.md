# `set.issuperset()` — 集合方法

> **功能：** 检查当前集合是否包含 other 中的所有成员。

<a href="../../../../tools/containers.html#set.issuperset">在交互式图鉴中查看这个方法的操作图解</a>

## 调用形式

```python
s.issuperset(other)
```

## 参数说明

- **`other`**（集合或可迭代对象）：被检查是否全部落在当前集合中。

**返回值：** bool（True/False）

**是否修改原容器：** 否。

## 时间复杂度

**两个 set 平均 O(|other|)，可提前失败**

解释：遍历 other 的成员并在当前集合里做哈希查询。

## 可运行示例

```python
a = {1, 2, 3}
b = {1, 2}
print(a.issuperset(b))
print(b.issuperset(a))
```

输出：

```text
True
False
```

## 执行过程

1. 确认 b 的 1、2 都包含在 a 里。
2. a 是 b 的超集，返回 True。
3. b 缺少 3，因此反向返回 False。

## 常见错误与风险

- A >= B 允许两者相等；A > B 是严格真超集。
- 对于一般可迭代对象，实际成本还受输入遍历影响。

## 参考依据

- [Python 官方文档：Built-in Types（内置类型）](https://docs.python.org/3/library/stdtypes.html)
- [Python Wiki：TimeComplexity（CPython 常见时间复杂度）](https://wiki.python.org/moin/TimeComplexity)
