# `dict.copy()` — 字典方法

> **功能：** 浅拷贝字典：外层键值结构独立，内部可变对象共享。

<a href="../../../../tools/containers.html#dict.copy">在交互式图鉴中查看这个方法的操作图解</a>

## 调用形式

```python
other = d.copy()
```

## 参数说明

本方法不需要额外参数。

**返回值：** 新字典对象

**是否修改原容器：** 否：d 不直接改变。

## 时间复杂度

**O(n)**

解释：复制键值槽与引用。

## 可运行示例

```python
d = {"scores": [80]}
other = d.copy()
other["scores"].append(90)
print(d)
print(other)
```

输出：

```text
{'scores': [80, 90]}
{'scores': [80, 90]}
```

## 执行过程

1. 创建新的外层字典 other。
2. scores 对应的列表仍是共享的。
3. 对这个共享列表追加 90，两个字典均可见。

## 常见错误与风险

- copy() 不会递归复制值中的列表、字典。
- 复制后重新赋值 other["x"] 不影响 d，但修改共享子列表会影响 d。

## 参考依据

- [Python 官方文档：Built-in Types（内置类型）](https://docs.python.org/3/library/stdtypes.html)
- [Python Wiki：TimeComplexity（CPython 常见时间复杂度）](https://wiki.python.org/moin/TimeComplexity)
