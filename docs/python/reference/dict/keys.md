# `dict.keys()` — 字典方法

> **功能：** 返回键的动态视图：可以遍历所有键，随字典内容变化。

<a href="../../../../tools/containers.html#dict.keys">在交互式图鉴中查看这个方法的操作图解</a>

## 调用形式

```python
d.keys()
```

## 参数说明

本方法不需要额外参数。

**返回值：** dict_keys 视图

**是否修改原容器：** 否；修改字典会反映在视图中。

## 时间复杂度

**O(1) 创建视图；遍历 O(n)**

解释：只构造一个轻量视图对象，没有复制所有键。

## 可运行示例

```python
d = {"a": 1}
v = d.keys()
d["b"] = 2
print(list(v))
```

输出：

```text
['a', 'b']
```

## 执行过程

1. keys() 获取与 d 关联的视图 v。
2. 随后给 d 增加键 b。
3. list(v) 此时读到 a 和 b 两个键。

## 常见错误与风险

- 视图不是普通列表，不能使用 v[0] 直接索引。
- 遍历期间增删键，通常会引发 RuntimeError，不要依赖可继续遍历。

## 参考依据

- [Python 官方文档：Built-in Types（内置类型）](https://docs.python.org/3/library/stdtypes.html)
- [Python Wiki：TimeComplexity（CPython 常见时间复杂度）](https://wiki.python.org/moin/TimeComplexity)
