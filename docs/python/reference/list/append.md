# `list.append()` — 列表方法

> **功能：** 在列表末尾添加一个元素；传入的对象整体作为一个元素。

<a href="../../../../tools/containers.html#list.append">在交互式图鉴中查看这个方法的操作图解</a>

## 调用形式

```python
a.append(item)
```

## 参数说明

- **`item`**（任意对象）：要追加的单个元素；即使传入列表，也不会拆开。

**返回值：** None（空值）

**是否修改原容器：** 是：原列表长度增加。

## 时间复杂度

**均摊 O(1)**

解释：动态数组通常预留容量；容量耗尽扩容时单次可能 O(n)。

## 可运行示例

```python
a = [1, 2]
a.append(3)
print(a)
print(a.append([4, 5]))
print(a)
```

输出：

```text
[1, 2, 3]
None
[1, 2, 3, [4, 5]]
```

## 执行过程

1. a 初始保存两个元素 1、2。
2. append(3) 在末尾写入一个整数。
3. append([4, 5]) 会追加完整子列表；返回值是 None。

## 常见错误与风险

- append([3, 4]) 会把 [3, 4] 作为一个嵌套元素。
- 不要写 b = a.append(3)：b 会是 None。

## 参考依据

- [Python 官方文档：Built-in Types（内置类型）](https://docs.python.org/3/library/stdtypes.html)
- [Python Wiki：TimeComplexity（CPython 常见时间复杂度）](https://wiki.python.org/moin/TimeComplexity)
