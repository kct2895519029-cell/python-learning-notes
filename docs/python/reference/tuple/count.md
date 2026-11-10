# `tuple.count()` — 元组方法

> **功能：** 计算目标值在元组中出现的次数。

<a href="../../../../tools/containers.html#tuple.count">在交互式图鉴中查看这个方法的操作图解</a>

## 调用形式

```python
t.count(value)
```

## 参数说明

- **`value`**（任意可比较对象）：使用 == 比较元素值。

**返回值：** 整数（次数）

**是否修改原容器：** 否。

## 时间复杂度

**O(n)**

解释：扫描所有元素。

## 可运行示例

```python
t = (1, True, 2, 1.0)
print(t.count(1))
```

输出：

```text
3
```

## 执行过程

1. 每个元素依次与 1 比较。
2. 1、True、1.0 都等于 1。
3. 返回次数 3。

## 常见错误与风险

- True、1、1.0 之间的相等比较可能得到 True，因此不是严格类型计数。

## 参考依据

- [Python 官方文档：Built-in Types（内置类型）](https://docs.python.org/3/library/stdtypes.html)
- [Python Wiki：TimeComplexity（CPython 常见时间复杂度）](https://wiki.python.org/moin/TimeComplexity)
