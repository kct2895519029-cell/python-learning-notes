# `list.remove()` — 列表方法

> **功能：** 查找并删除首个与 value 相等的元素。

<a href="../../../../tools/containers.html#list.remove">在交互式图鉴中查看这个方法的操作图解</a>

## 调用形式

```python
a.remove(value)
```

## 参数说明

- **`value`**（任意可比较对象）：用相等比较（==）寻找第一次出现的位置。

**返回值：** None

**是否修改原容器：** 是。

## 时间复杂度

**O(n)**

解释：最坏需要线性扫描整个列表，删除后还可能移动元素。

## 可运行示例

```python
a = [2, 3, 2, 4]
a.remove(2)
print(a)
```

输出：

```text
[3, 2, 4]
```

## 执行过程

1. 从左往右比较元素是否等于 2。
2. 第一个位置匹配，删除该元素。
3. 后面仍保留第二个 2。

## 常见错误与风险

- 未找到值抛 ValueError。
- 只删除第一个，不删除所有重复值。
- 遍历原列表时直接 remove 易跳过相邻元素。

## 参考依据

- [Python 官方文档：Built-in Types（内置类型）](https://docs.python.org/3/library/stdtypes.html)
- [Python Wiki：TimeComplexity（CPython 常见时间复杂度）](https://wiki.python.org/moin/TimeComplexity)
