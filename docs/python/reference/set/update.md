# `set.update()` — 集合方法

> **功能：** 遍历一个或多个可迭代对象，逐个把元素加入集合。

<a href="../../../../tools/containers.html#set.update">在交互式图鉴中查看这个方法的操作图解</a>

## 调用形式

```python
s.update(*iterables)
```

## 参数说明

- **`*iterables`**（多个可迭代对象）：如列表、集合、字符串；逐个取出其元素并加入。

**返回值：** None

**是否修改原容器：** 可能修改。

## 时间复杂度

**均摊 O(k)，k 为输入元素总数**

解释：对每个输入元素执行哈希添加；重复元素仍需检查。

## 可运行示例

```python
s = {1}
s.update([1, 2], [3])
print(sorted(s))
```

输出：

```text
[1, 2, 3]
```

## 执行过程

1. 遍历 [1, 2]：1 已有，新增 2。
2. 继续遍历 [3]：新增 3。
3. 最终集合成员为 1、2、3。

## 常见错误与风险

- update("ab") 会加入 "a" 和 "b" 两个字符。
- 与 dict.update 的“键值对更新”完全不同。

## 参考依据

- [Python 官方文档：Built-in Types（内置类型）](https://docs.python.org/3/library/stdtypes.html)
- [Python Wiki：TimeComplexity（CPython 常见时间复杂度）](https://wiki.python.org/moin/TimeComplexity)
