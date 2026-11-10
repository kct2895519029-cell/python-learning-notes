#!/usr/bin/env python3
"""创建新的 Markdown 学习笔记；MkDocs 自动识别新文件。"""
from pathlib import Path
import argparse
import re

ROOT = Path(__file__).resolve().parent.parent
DOCUMENTS = ROOT / 'docs'

def main():
    parser = argparse.ArgumentParser(description='创建 Python & AI 学习笔记')
    parser.add_argument('--section', choices=['python', 'ai', 'journal'], required=True,
                        help='笔记分区')
    parser.add_argument('--slug', required=True, help='文件名：仅小写英文/数字/连字符')
    parser.add_argument('--title', required=True, help='显示在网页中的中文标题')
    args = parser.parse_args()
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', args.slug):
        parser.error('slug 必须使用小写英文、数字和连字符，例如 api-first-request')
    path = DOCUMENTS / args.section / (args.slug+'.md')
    if path.exists():
        parser.error(f'已有同名笔记，拒绝覆盖：{path}')
    content = f"""# {args.title}

> 状态：学习中 | 来源：待补充 | 更新日期：待填写

## 一、先给结论

简要说明本节最重要的结论。

## 二、核心概念与中文解释

- **英文术语（中文）**：白话解释 + 一个具体例子。

## 三、整体数据流与调用链

输入 → 处理 → 输出

## 四、完整的最小代码实例

```python
# 代码放在这里；注明 Python 版本和依赖
```

## 五、逐行解释

说明每行函数、变量、参数、返回值及执行顺序。

## 六、实际输出与验证

记录在本地运行得到的输出，不要编造实验结果。

## 七、常见错误与复盘

| 现象 | 原因 | 解决办法 |
|---|---|---|
| 待填写 | 待填写 | 待填写 |

## 八、练习与自测

1. 练习题：待补充。

## 九、参考资料

- 官方文档、论文标题、版本及链接：待补充。
"""
    path.write_text(content, encoding='utf-8')
    print('Created:', path.relative_to(ROOT))
    print('下一步：编辑该 Markdown 文件，运行 mkdocs serve，然后 git commit/push。')

if __name__ == '__main__':
    main()
