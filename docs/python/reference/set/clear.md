# `set.clear()` — 集合方法

> **功能：** 清空整个集合，保留原集合对象。

<a href="../../../../tools/containers.html#set.clear">在交互式图鉴中查看这个方法的操作图解</a>

## 调用形式

```python
s.clear()
```

## 参数说明

本方法不需要额外参数。

**返回值：** None

**是否修改原容器：** 是。

## 时间复杂度

**O(n)**

解释：解除每个成员引用并清除内部表。

## 可运行示例

```python
s = {1, 2}
alias = s
s.clear()
print(s)
print(alias)
```

输出：

```text
set()
set()
```

## 执行过程

1. alias 和 s 共享同一集合对象。
2. clear() 使集合变空。
3. 两者打印结果都为 set()。

## 常见错误与风险

- 若多个变量引用同一个集合，clear 会影响所有别名。
- 空集合是 set()，{} 则是空字典。

## 参考依据

- [Python 官方文档：Built-in Types（内置类型）](https://docs.python.org/3/library/stdtypes.html)
- [Python Wiki：TimeComplexity（CPython 常见时间复杂度）](https://wiki.python.org/moin/TimeComplexity)
