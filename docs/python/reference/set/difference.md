# `set.difference()` — 集合方法

> **功能：** 计算差集：保留当前集合中存在、其他输入中不存在的成员。

<a href="../../../../tools/containers.html#set.difference">在交互式图鉴中查看这个方法的操作图解</a>

## 调用形式

```python
s.difference(*others)
```

## 参数说明

- **`*others`**（一个或多个可迭代对象）：依次排除其中出现的成员。

**返回值：** 新的 set 集合

**是否修改原容器：** 否。

## 时间复杂度

**两个 set 常见 O(|A|)，非 set 输入另计**

解释：典型 set-set 情形复制/扫描 A；实现与多输入和类型有关。

## 可运行示例

```python
a = {1, 2, 3}
b = {2, 4}
print(sorted(a.difference(b)))
print(sorted(b.difference(a)))
```

输出：

```text
[1, 3]
[4]
```

## 执行过程

1. A 独有的成员是 1、3。
2. B 独有的成员是 4。
3. 两个方向结果不同。

## 常见错误与风险

- A - B 与 B - A 通常不同；差集没有交换律。
- difference([2]) 合法，但 A - [2] 不合法。

## 参考依据

- [Python 官方文档：Built-in Types（内置类型）](https://docs.python.org/3/library/stdtypes.html)
- [Python Wiki：TimeComplexity（CPython 常见时间复杂度）](https://wiki.python.org/moin/TimeComplexity)
