# `list.reverse()` — 列表方法

> **功能：** 不比较元素大小，直接把当前顺序反过来。

<a href="../../../../tools/containers.html#list.reverse">在交互式图鉴中查看这个方法的操作图解</a>

## 调用形式

```python
a.reverse()
```

## 参数说明

本方法不需要额外参数。

**返回值：** None

**是否修改原容器：** 是。

## 时间复杂度

**O(n)**

解释：把头尾元素交换，逐步向中间推进。

## 可运行示例

```python
a = [3, 1, 2]
a.reverse()
print(a)
```

输出：

```text
[2, 1, 3]
```

## 执行过程

1. 最左边 3 与最右边 2 交换。
2. 中间 1 的位置不变。
3. 最终仅翻转顺序为 [2, 1, 3]。

## 常见错误与风险

- reverse() 不是按值大小排序。
- 和 reversed(a) 不同：后者返回反向迭代器，不修改 a。

## 参考依据

- [Python 官方文档：Built-in Types（内置类型）](https://docs.python.org/3/library/stdtypes.html)
- [Python Wiki：TimeComplexity（CPython 常见时间复杂度）](https://wiki.python.org/moin/TimeComplexity)
