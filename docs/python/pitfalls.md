# 高频坑点与纠错

以下是容易导致程序出现隐蔽错误的操作。先判断**会不会修改原对象**，再判断**返回值是什么**。

## 1. `append` 和 `extend` 不一样

```python
a = [1]
a.append([2, 3])
print(a)            # [1, [2, 3]]

b = [1]
b.extend([2, 3])
print(b)            # [1, 2, 3]
```

- `append(item)`：整体追加一个对象。
- `extend(iterable)`：从可迭代对象中逐个获取元素追加。

## 2. 别把原地修改方法的返回值赋给原变量

```python
a = [3, 1, 2]
result = a.sort()
print(a)       # [1, 2, 3]
print(result)  # None
```

`sort()` 修改 `a` 本身，返回 `None`。若需要新列表，可以使用 `sorted(a)`。

## 3. `get` 和 `setdefault` 不是同一个操作

```python
d = {}
print(d.get("items", []))       # []
print(d)                        # {}
d.setdefault("items", []).append(1)
print(d)                        # {'items': [1]}
```

`get` 不插入；`setdefault` 在键缺失时会插入默认值。

## 4. 遍历时直接删除元素容易漏掉数据

```python
a = [2, 2, 3]
for x in a:
    if x == 2:
        a.remove(x)
print(a)  # [2, 3]：还剩下一个 2
```

适合创建新列表时可以使用推导式：

```python
a = [2, 2, 3]
a = [x for x in a if x != 2]
print(a)  # [3]
```

## 5. `1`、`True` 和 `1.0` 在相等判断中可能匹配

```python
print([1, True, 1.0].count(1))  # 3
print(len({1, True, 1.0}))      # 1
```

不要把 `==` 当作“类型和数值都必须相同”的检查。如果确实需要同时比较类型，可以结合 `type(x) is type(target)` 使用。

## 6. 集合的 `pop()` 不是随机抽样

`set.pop()` 删除任意一个元素，但不保证均匀随机，不能代替抽样算法。输出集合时通常也不能依赖其顺序。

## 7. `tuple` 的不可变约束是针对成员引用

```python
t = ([1, 2], "x")
t[0].append(3)
print(t)  # ([1, 2, 3], 'x')
```

不能替换 `t[0]`，但其引用的列表内容可以改变。

## 8. 操作复杂度有前提

- 列表 `append` 的 **均摊 O(1)** 不代表每次都严格 O(1)。
- 哈希表查找的 **平均 O(1)** 假设哈希计算、相等比较和冲突行为处于一般情况。
- 集合交集的 O(min(|A|, |B|)) 主要适用于双方都是集合的常见实现情况；一般可迭代输入可能有额外遍历或转换成本。

更多细节可进入 <a href="../../tools/containers.html">交互式方法图鉴</a>。
