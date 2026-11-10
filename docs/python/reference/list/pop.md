# `list.pop()` — 列表方法

> **功能：** 删除指定索引的元素，并把它作为返回值交给调用方。

<a href="../../../../tools/containers.html#list.pop">在交互式图鉴中查看这个方法的操作图解</a>

## 调用形式

```python
a.pop(index=-1)
```

## 参数说明

- **`index`**（整数，可选；默认 -1）：省略时删除末尾；0 表示第一个元素。

**返回值：** 被删除的元素

**是否修改原容器：** 是：删除一个元素。

## 时间复杂度

**尾部均摊 O(1)；其他位置 O(n)**

解释：从中间删除需要左移后续元素。

## 可运行示例

```python
a = [10, 20, 30]
x = a.pop(1)
print(x)
print(a)
print(a.pop())
print(a)
```

输出：

```text
20
[10, 30]
30
[10]
```

## 执行过程

1. pop(1) 读取并删除索引 1 的 20。
2. x 接住删除的值 20。
3. 第二次 pop() 默认删除末尾 30。

## 常见错误与风险

- 空列表 pop() 或越界索引都会抛 IndexError。
- pop 是按位置删除，remove 是按值删除。

## 参考依据

- [Python 官方文档：Built-in Types（内置类型）](https://docs.python.org/3/library/stdtypes.html)
- [Python Wiki：TimeComplexity（CPython 常见时间复杂度）](https://wiki.python.org/moin/TimeComplexity)
