#!/usr/bin/env python3
"""为每个容器方法从 JSON 生成独立 Markdown 页面，以便网站全文搜索。"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / 'data' / 'containers.json'
DOCS = ROOT / 'docs' / 'python' / 'reference'
NAMES = {'list':'列表','dict':'字典','tuple':'元组','set':'集合'}


def main() -> int:
    methods = json.loads(DATA.read_text(encoding='utf-8'))
    counts = {category: 0 for category in NAMES}
    for method in methods:
        cat = method['cat']
        if cat not in NAMES:
            raise ValueError(f'未知类别: {cat}')
        counts[cat] += 1
        dst = DOCS / cat / (method['name']+'.md')
        dst.parent.mkdir(parents=True, exist_ok=True)
        params = method['params'] or []
        para_md = '\n'.join(f"- **`{p['name']}`**（{p['type']}）：{p['desc']}" for p in params) or '本方法不需要额外参数。'
        steps_md = '\n'.join(f'{i}. {step}' for i, step in enumerate(method['steps'], start=1))
        pitfalls_md = '\n'.join(f'- {text}' for text in method['pitfalls'])
        src_link = f'../../../../tools/containers.html#{method["id"]}'
        content = f'''# `{method['id']}()` — {NAMES[cat]}方法

> **功能：** {method['desc']}

<a href="{src_link}">在交互式图鉴中查看这个方法的操作图解</a>

## 调用形式

```python
{method['sig']}
```

## 参数说明

{para_md}

**返回值：** {method['ret']}

**是否修改原容器：** {method['mutate']}

## 时间复杂度

**{method['cost']}**

解释：{method['why']}

## 可运行示例

```python
{method['code']}
```

输出：

```text
{method['output']}
```

## 执行过程

{steps_md}

## 常见错误与风险

{pitfalls_md}

## 参考依据

- [Python 官方文档：Built-in Types（内置类型）](https://docs.python.org/3/library/stdtypes.html)
- [Python Wiki：TimeComplexity（CPython 常见时间复杂度）](https://wiki.python.org/moin/TimeComplexity)
'''
        dst.write_text(content, encoding='utf-8')
    print(f'Generated {sum(counts.values())} indexed Markdown method pages: {counts}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
