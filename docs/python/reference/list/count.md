# `list.count()` — 列表方法

> **功能：** 统计列表中与目标值相等的元素出现次数。

<a href="../../../../tools/containers.html#list.count">在交互式图鉴中查看这个方法的操作图解</a>

## 调用形式

```python
a.count(value)
```

## 参数说明

- **`value`**（任意可比较对象）：用 == 逐一比较，不要求类型完全一致。

**返回值：** 整数（次数）

**是否修改原容器：** 否。

## 时间复杂度

**O(n)**

解释：必须遍历所有元素计数。

## 可运行示例

```python
a = [1, True, 1.0, 2]
print(a.count(1))
```

输出：

```text
3
```

## 执行过程

1. count(1) 逐个执行相等比较。
2. 1、True、1.0 都满足 == 1。
3. 因此总次数为 3。

## 常见错误与风险

- 1 == 1.0 == True 为真，统计并不按“同类型”严格匹配。
- 复杂对象的 == 可能比较昂贵。

## 参考依据

- [Python 官方文档：Built-in Types（内置类型）](https://docs.python.org/3/library/stdtypes.html)
- [Python Wiki：TimeComplexity（CPython 常见时间复杂度）](https://wiki.python.org/moin/TimeComplexity)
