# `set.pop()` — 集合方法

> **功能：** 移除并返回集合里的一个任意元素。

<a href="../../../../tools/containers.html#set.pop">在交互式图鉴中查看这个方法的操作图解</a>

## 调用形式

```python
s.pop()
```

## 参数说明

本方法不需要额外参数。

**返回值：** 被删除的元素

**是否修改原容器：** 是。

## 时间复杂度

**平均 O(1)**

解释：实现通过内部表寻找可用条目；不保证特定成员。

## 可运行示例

```python
s = {1, 2, 3}
x = s.pop()
print(x in {1, 2, 3})
print(len(s))
```

输出：

```text
True
2
```

## 执行过程

1. pop() 返回集合中的某个成员；无法指定哪个。
2. 被返回的值属于原始集合，因此判断为 True。
3. 移除一个后长度为 2。

## 常见错误与风险

- 任意元素≠统计意义上的随机抽样；不要依赖具体结果或顺序。
- 空集合 pop() 抛 KeyError。

## 参考依据

- [Python 官方文档：Built-in Types（内置类型）](https://docs.python.org/3/library/stdtypes.html)
- [Python Wiki：TimeComplexity（CPython 常见时间复杂度）](https://wiki.python.org/moin/TimeComplexity)
