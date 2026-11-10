#!/usr/bin/env python3
"""逐项验证交互式方法图鉴的最小代码示例和预期输出。"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
entries = json.loads((ROOT/'data'/'containers.json').read_text(encoding='utf-8'))
failures = []
for item in entries:
    result = subprocess.run([sys.executable, '-I', '-c', item['code']],
                            capture_output=True, text=True, timeout=8)
    actual = result.stdout.strip().replace('\r\n','\n')
    expected = item['output'].strip().replace('\r\n','\n')
    if result.returncode != 0 or actual != expected:
        failures.append((item['id'], expected, actual, result.stderr))
for id_, exp, got, err in failures:
    print(f'FAIL {id_}\n expected: {exp!r}\n actual:   {got!r}\n {err}')
print(f'Checked {len(entries)} runnable examples; errors: {len(failures)}')
sys.exit(1 if failures else 0)
