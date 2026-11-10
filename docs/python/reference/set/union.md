# `set.union()` — 集合方法

> **功能：** 计算并集：保留任意输入中出现过的成员，返回新集合。

<a href="../../../../tools/containers.html#set.union">在交互式图鉴中查看这个方法的操作图解</a>

## 调用形式

```python
s.union(*others)
```

## 参数说明

- **`*others`**（一个或多个可迭代对象）：如 set、list；方法允许多种可迭代对象。

**返回值：** 新的 set 集合

**是否修改原容器：** 否。

## 时间复杂度

**常见两个集合 O(|A|+|B|)**

解释：复制 A 并扫描 B 加入成员；多集合扩展为各输入规模总和。

## 可运行示例

```python
a = {1, 2}
b = {2, 3}
c = a.union(b)
print(sorted(c))
print(sorted(a))
```

输出：

```text
[1, 2, 3]
[1, 2]
```

## 执行过程

1. 先将 a 的成员复制到新集合。
2. 把 b 中尚未出现的 3 加入。
3. c 是新集合，原 a 仍为 {1,2}。

## 常见错误与风险

- s.union([2,3]) 合法，但 s | [2,3] 不合法（运算符一般要求集合类操作数）。
- 并集返回新集合，除非赋值回原变量否则原集合不变。

## 参考依据

- [Python 官方文档：Built-in Types（内置类型）](https://docs.python.org/3/library/stdtypes.html)
- [Python Wiki：TimeComplexity（CPython 常见时间复杂度）](https://wiki.python.org/moin/TimeComplexity)
