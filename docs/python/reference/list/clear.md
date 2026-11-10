# `list.clear()` — 列表方法

> **功能：** 原地删除列表中的全部元素。

<a href="../../../../tools/containers.html#list.clear">在交互式图鉴中查看这个方法的操作图解</a>

## 调用形式

```python
a.clear()
```

## 参数说明

本方法不需要额外参数。

**返回值：** None

**是否修改原容器：** 是：列表变空。

## 时间复杂度

**O(n)**

解释：需要逐个解除对原元素的引用；释放内存成本视对象而定。

## 可运行示例

```python
a = [1, 2]
b = a
a.clear()
print(a)
print(b)
```

输出：

```text
[]
[]
```

## 执行过程

1. b = a 表示两个变量指向同一个列表对象。
2. clear() 修改这个共同对象。
3. 因此 a 与 b 读到的都是空列表。

## 常见错误与风险

- 其他变量若引用的是同一个列表，也会看到空列表。
- a = [] 只重新绑定变量 a，不会清空别名所指旧列表。

## 参考依据

- [Python 官方文档：Built-in Types（内置类型）](https://docs.python.org/3/library/stdtypes.html)
- [Python Wiki：TimeComplexity（CPython 常见时间复杂度）](https://wiki.python.org/moin/TimeComplexity)
