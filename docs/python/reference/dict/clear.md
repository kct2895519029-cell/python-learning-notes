# `dict.clear()` — 字典方法

> **功能：** 原地移除全部键值对。

<a href="../../../../tools/containers.html#dict.clear">在交互式图鉴中查看这个方法的操作图解</a>

## 调用形式

```python
d.clear()
```

## 参数说明

本方法不需要额外参数。

**返回值：** None

**是否修改原容器：** 是。

## 时间复杂度

**O(n)**

解释：须清除每个键和值的引用并处理存储。

## 可运行示例

```python
d = {"a": 1}
alias = d
d.clear()
print(d)
print(alias)
```

输出：

```text
{}
{}
```

## 执行过程

1. alias 和 d 指向同一个字典。
2. clear() 清空这一对象。
3. 两个变量均显示 {}。

## 常见错误与风险

- 所有指向同一字典对象的变量都会看到空字典。
- 别混淆 d.clear() 与把 d 重新赋值为 {}。

## 参考依据

- [Python 官方文档：Built-in Types（内置类型）](https://docs.python.org/3/library/stdtypes.html)
- [Python Wiki：TimeComplexity（CPython 常见时间复杂度）](https://wiki.python.org/moin/TimeComplexity)
