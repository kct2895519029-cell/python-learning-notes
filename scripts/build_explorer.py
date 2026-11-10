#!/usr/bin/env python3
"""用结构化 JSON 生成交互式方法图鉴 HTML，避免每次手工编辑长网页。"""
from pathlib import Path
import json
import sys

BASE = Path(__file__).resolve().parent.parent
DATA = BASE / 'data' / 'containers.json'
TEMPLATE = BASE / 'site_src' / 'containers.html.template'
DEST = BASE / 'docs' / 'tools' / 'containers.html'

def main() -> int:
    methods = json.loads(DATA.read_text(encoding='utf-8'))
    seen = set()
    for item in methods:
        assert all(k in item for k in ('id','cat','name','code','output')), item
        assert item['id'] not in seen, f"方法 ID 重复：{item['id']}"
        seen.add(item['id'])
    html = TEMPLATE.read_text(encoding='utf-8')
    if '__METHOD_JSON__' not in html:
        raise ValueError('模板中缺失数据插入标记')
    # 不将外部文字解释为脚本结束标签；避免破坏 JSON 数据区域。
    payload = json.dumps(methods, ensure_ascii=False).replace('<', r'\u003c')
    html = html.replace('__METHOD_JSON__', payload)
    html = html.replace('<strong>36</strong> 方法', f'<strong>{len(methods)}</strong> 方法')
    html = html.replace('36 种内置方法', f'{len(methods)} 种内置方法')
    DEST.parent.mkdir(parents=True, exist_ok=True)
    DEST.write_text(html, encoding='utf-8')
    print(f'Generated: {DEST.relative_to(BASE)} ({len(methods)} methods)')
    return 0

if __name__ == '__main__':
    sys.exit(main())
