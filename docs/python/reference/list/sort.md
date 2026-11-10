# `list.sort()` — 列表方法

> **功能：** 在原列表上排序，支持自定义排序依据和升降序。

<a href="../../../../tools/containers.html#list.sort">在交互式图鉴中查看这个方法的操作图解</a>

## 调用形式

```python
a.sort(key=None, reverse=False)
```

## 参数说明

- **`key`**（函数或 None）：元素映射到比较键；如 abs、str.lower。
- **`reverse`**（布尔值；默认 False）：True 为降序，False 为升序；只允许按关键字传参。

**返回值：** None

**是否修改原容器：** 是：元素原地重排。

## 时间复杂度

**最坏/平均 O(n log n)，近乎有序可 O(n)**

解释：CPython 使用稳定自适应排序（Timsort 体系）；计算 key 的成本另计。

## 可运行示例

```python
a = [-5, 2, -1, 3]
a.sort(key=abs, reverse=True)
print(a)
```

输出：

```text
[-5, 3, 2, -1]
```

## 执行过程

1. key=abs 取绝对值作比较依据：5、2、1、3。
2. reverse=True 使比较依据从大到小。
3. 原列表元素被重排为 [-5, 3, 2, -1]。

## 常见错误与风险

- sort() 返回 None，不是排序后的列表。
- 混合类型不必然报错：只要排序键可比较即可。
- 排序是稳定的：相同 key 的原有顺序保持不变。

## 参考依据

- [Python 官方文档：Built-in Types（内置类型）](https://docs.python.org/3/library/stdtypes.html)
- [Python Wiki：TimeComplexity（CPython 常见时间复杂度）](https://wiki.python.org/moin/TimeComplexity)
