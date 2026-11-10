# `dict.items()` — 字典方法

> **功能：** 返回键值对的动态视图，迭代得到 (key, value) 元组。

<a href="../../../../tools/containers.html#dict.items">在交互式图鉴中查看这个方法的操作图解</a>

## 调用形式

```python
d.items()
```

## 参数说明

本方法不需要额外参数。

**返回值：** dict_items 视图

**是否修改原容器：** 否。

## 时间复杂度

**O(1) 创建；遍历 O(n)**

解释：只构造视图；每次迭代产生对应键值对。

## 可运行示例

```python
d = {"name": "Li", "age": 20}
for key, value in d.items():
    print(key, value)
```

输出：

```text
name Li
age 20
```

## 执行过程

1. items() 在循环中依次提供 (键, 值) 二元组。
2. for key, value 把二元组拆给两个变量。
3. 打印每组键和值。

## 常见错误与风险

- for key, value in d.items() 是最常见的解包形式。
- 迭代期间改变字典大小会有风险。

## 参考依据

- [Python 官方文档：Built-in Types（内置类型）](https://docs.python.org/3/library/stdtypes.html)
- [Python Wiki：TimeComplexity（CPython 常见时间复杂度）](https://wiki.python.org/moin/TimeComplexity)
