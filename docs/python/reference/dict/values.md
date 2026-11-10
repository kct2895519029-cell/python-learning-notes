# `dict.values()` — 字典方法

> **功能：** 返回值的动态视图，按字典的插入顺序遍历值。

<a href="../../../../tools/containers.html#dict.values">在交互式图鉴中查看这个方法的操作图解</a>

## 调用形式

```python
d.values()
```

## 参数说明

本方法不需要额外参数。

**返回值：** dict_values 视图

**是否修改原容器：** 否。

## 时间复杂度

**O(1) 创建；遍历 O(n)**

解释：视图没有立即复制每个值。

## 可运行示例

```python
d = {"a": 1}
v = d.values()
d["b"] = 2
print(list(v))
```

输出：

```text
[1, 2]
```

## 执行过程

1. 获取动态值视图 v。
2. 新增键 b 对应值 2。
3. 从 v 读取时看到 1、2。

## 常见错误与风险

- 值视图不可通过下标取第一个值。
- values() 的两个视图相互比较，即使来自同一字典通常也不相等。

## 参考依据

- [Python 官方文档：Built-in Types（内置类型）](https://docs.python.org/3/library/stdtypes.html)
- [Python Wiki：TimeComplexity（CPython 常见时间复杂度）](https://wiki.python.org/moin/TimeComplexity)
