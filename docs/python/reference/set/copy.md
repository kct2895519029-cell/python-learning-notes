# `set.copy()` — 集合方法

> **功能：** 浅拷贝集合，返回具有相同成员的新集合。

<a href="../../../../tools/containers.html#set.copy">在交互式图鉴中查看这个方法的操作图解</a>

## 调用形式

```python
t = s.copy()
```

## 参数说明

本方法不需要额外参数。

**返回值：** 新的 set 集合

**是否修改原容器：** 否。

## 时间复杂度

**O(n)**

解释：须把原集合的成员引用复制进新哈希表。

## 可运行示例

```python
s = {1, 2}
t = s.copy()
t.add(3)
print(sorted(s))
print(sorted(t))
print(s is t)
```

输出：

```text
[1, 2]
[1, 2, 3]
False
```

## 执行过程

1. t 是独立的新集合对象。
2. 修改 t 新增 3 不影响 s。
3. s is t 返回 False。

## 常见错误与风险

- set 的成员必须可哈希；通常不会直接包含普通 list/dict。
- 若成员是“可哈希但内部可变”的自定义对象，浅拷贝也不会复制它。

## 参考依据

- [Python 官方文档：Built-in Types（内置类型）](https://docs.python.org/3/library/stdtypes.html)
- [Python Wiki：TimeComplexity（CPython 常见时间复杂度）](https://wiki.python.org/moin/TimeComplexity)
