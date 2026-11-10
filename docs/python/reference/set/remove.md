# `set.remove()` — 集合方法

> **功能：** 从集合中删除指定成员；不存在时抛异常。

<a href="../../../../tools/containers.html#set.remove">在交互式图鉴中查看这个方法的操作图解</a>

## 调用形式

```python
s.remove(item)
```

## 参数说明

- **`item`**（待删除元素）：按哈希及相等语义定位。

**返回值：** None

**是否修改原容器：** 是：当元素存在时删除。

## 时间复杂度

**平均 O(1)**

解释：哈希查找删除目标成员。

## 可运行示例

```python
s = {1, 2, 3}
s.remove(2)
print(sorted(s))
```

输出：

```text
[1, 3]
```

## 执行过程

1. 查找并删除成员 2。
2. 其他成员 1、3 保留。
3. sorted 仅用于让输出顺序稳定。

## 常见错误与风险

- 目标不存在抛 KeyError。
- 若不确定元素是否存在且希望不报错，使用 discard。

## 参考依据

- [Python 官方文档：Built-in Types（内置类型）](https://docs.python.org/3/library/stdtypes.html)
- [Python Wiki：TimeComplexity（CPython 常见时间复杂度）](https://wiki.python.org/moin/TimeComplexity)
