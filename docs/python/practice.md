# Python 容器：练习与自测

将下面代码复制到 PyCharm，**先预测输出，再运行对照**。不要只记忆方法名称。

## 练习 1：嵌套列表

```python
a = [1, 2]
a.append([3, 4])
a.extend([5, 6])
print(a)
print(len(a))
```

??? question "参考答案与原因"
    输出为 `[1, 2, [3, 4], 5, 6]` 和 `5`。`append` 一次增加一个列表元素；`extend` 逐个增加 5、6。

## 练习 2：字典是否被修改

```python
d = {"x": None}
a = d.get("y", 0)
b = d.setdefault("y", 0)
print(a, b, d)
```

??? question "参考答案与原因"
    输出 `0 0 {'x': None, 'y': 0}`。`get` 不修改字典；`setdefault` 对缺失的 y 插入 0。

## 练习 3：别名与浅拷贝

```python
a = [[1]]
b = a
c = a.copy()
c[0].append(2)
print(a, b, c)
print(a is b, a is c)
```

??? question "参考答案与原因"
    三份内容都是 `[[1, 2]]`；身份比较为 `True False`。b 与 a 是同一外层列表；c 是新外层列表，但共享内部列表。

## 练习 4：集合运算

```python
a = {1, 2, 3}
b = {3, 4}
print(sorted(a & b))
print(sorted(a ^ b))
```

??? question "参考答案与原因"
    交集 `[3]`；对称差集 `[1, 2, 4]`。

## 练习 5：复杂度判断

同一个列表有 n 个元素。下面操作一般分别是什么时间复杂度？

```python
a.append(7)
a.insert(0, 7)
7 in a
a.sort()
```

??? question "参考答案与原因"
    依次为均摊 O(1)、O(n)、O(n)、最坏 O(n log n)，实际还有元素比较等成本。
