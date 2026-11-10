# `tuple.index()` — 元组方法

> **功能：** 在元组的指定区间中返回目标值的首个索引。

<a href="../../../../tools/containers.html#tuple.index">在交互式图鉴中查看这个方法的操作图解</a>

## 调用形式

```python
t.index(value, start=0, stop=len(t))
```

## 参数说明

- **`value`**（任意可比较对象）：按 == 比较。
- **`start`**（整数；默认 0）：包含该位置。
- **`stop`**（整数；默认元组长度）：不包含该位置。

**返回值：** 整数索引

**是否修改原容器：** 否：元组不可变。

## 时间复杂度

**O(n)**

解释：必须从左到右线性查找。

## 可运行示例

```python
t = ("a", "b", "a")
print(t.index("a", 1))
```

输出：

```text
2
```

## 执行过程

1. 从元组索引 1 开始检查。
2. 第 1 个元素 b 不匹配。
3. 第 2 个元素 a 匹配，所以返回 2。

## 常见错误与风险

- 找不到抛 ValueError。
- index 是查找位置，不是查找所有位置。

## 参考依据

- [Python 官方文档：Built-in Types（内置类型）](https://docs.python.org/3/library/stdtypes.html)
- [Python Wiki：TimeComplexity（CPython 常见时间复杂度）](https://wiki.python.org/moin/TimeComplexity)
