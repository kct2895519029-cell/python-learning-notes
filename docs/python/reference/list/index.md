# `list.index()` — 列表方法

> **功能：** 在指定查找区间内返回第一个匹配值的索引。

<a href="../../../../tools/containers.html#list.index">在交互式图鉴中查看这个方法的操作图解</a>

## 调用形式

```python
a.index(value, start=0, stop=len(a))
```

## 参数说明

- **`value`**（任意可比较对象）：目标值，使用 == 比较。
- **`start`**（整数，可选；默认 0）：搜索起点，包含本位置。
- **`stop`**（整数，可选；默认列表长度）：搜索终点，不包含本位置。

**返回值：** 整数索引

**是否修改原容器：** 否。

## 时间复杂度

**O(n)**

解释：线性扫描查找范围。

## 可运行示例

```python
a = ["a", "b", "a"]
print(a.index("a"))
print(a.index("a", 1))
```

输出：

```text
0
2
```

## 执行过程

1. 第一次从索引 0 开始找，返回 0。
2. 第二次从索引 1 开始找。
3. 索引 2 是下一次出现 "a" 的位置。

## 常见错误与风险

- 未找到时抛 ValueError。
- 区间是 [start, stop)，不含 stop。
- 先用 in 再 index 会重复查找；不确定时可用 try/except。

## 参考依据

- [Python 官方文档：Built-in Types（内置类型）](https://docs.python.org/3/library/stdtypes.html)
- [Python Wiki：TimeComplexity（CPython 常见时间复杂度）](https://wiki.python.org/moin/TimeComplexity)
