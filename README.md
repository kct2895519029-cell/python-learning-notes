# Python & AI 学习知识库

可长期维护的静态学习网站：MkDocs Material + 结构化 Python 方法图鉴 + Markdown 笔记 + GitHub Pages。

## 网站入口（GitHub Pages）

**学习网站入口：**

- [打开学习网站首页](https://kct2895519029-cell.github.io/python-learning-notes/)
- [打开 AI 应用开发学习专区](https://kct2895519029-cell.github.io/python-learning-notes/ai/)（目前为待补充的课程目录）
- [打开 Python 四大容器交互式方法图鉴](https://kct2895519029-cell.github.io/python-learning-notes/tools/containers.html)
- [查看网站部署状态（GitHub Actions）](https://github.com/kct2895519029-cell/python-learning-notes/actions)

**注意：** 当前 GitHub 的 `Code` 页面显示源代码；上面的 `github.io` 链接才是网站页面。网站由 GitHub Actions 从 `docs/` 下的 Markdown 文件构建并发布，**不必**在 `main` 分支中找到与网站页面地址同名的文件。

## 文件结构

```text
data/containers.json               四大容器 36 个方法的结构化数据（可维护）
site_src/containers.html.template  交互图鉴页面模板
scripts/build_explorer.py          从 JSON 生成网页
scripts/verify_examples.py         执行并核对图鉴代码与预期输出
scripts/new_note.py                创建一篇新 Markdown 学习笔记
docs/index.md                      网站首页
docs/python/                     Python 知识笔记
docs/ai/                         AI 应用开发知识笔记（待扩展）
docs/journal/                    学习日志与复盘
docs/tools/containers.html       自动生成的交互式方法图鉴
mkdocs.yml                       网站主题与配置
.github/workflows/deploy.yml     自动发布到 GitHub Pages
```

## 本地浏览

在 Windows PowerShell、Conda 的 Python 3.11 中：

```powershell
conda activate AI
python -m pip install -r requirements.txt
python scripts/build_explorer.py
python scripts/verify_examples.py
python -m mkdocs serve
```

浏览器打开终端显示的 `http://127.0.0.1:8000/`。

## 新增知识

网页导航自动发现 `docs/` 中新增的 Markdown 页面。只需新建 `docs/python/<slug>.md` 或 `docs/ai/<slug>.md`，添加正文并提交 GitHub。

命令生成示例：

```powershell
python scripts/new_note.py --section python --slug python-exceptions --title "Python 异常处理"
```

然后编辑新生成的文件并提交；不必手工修改 `mkdocs.yml` 的菜单。

## 更新四大容器的方法资料

修改 `data/containers.json` 中对应的条目；执行 `python scripts/build_explorer.py`，再使用浏览器检查。保留原方法的稳定 `id`，不要把代码的实际运行输出写成猜测结果。

## 部署到 GitHub Pages

1. 在 GitHub 创建一个独立仓库（例如 `python-learning-notes`）；若使用 GitHub Free 的 Pages 托管，仓库设为 Public。
2. 上传本工程文件（或通过 ChatGPT 已连接的 GitHub 仓库操作写入）。
3. 在仓库 `Settings → Pages → Build and deployment → Source` 选择 `GitHub Actions`。
4. 每次推送到 `main`，工作流会运行例子验证、生成图鉴、构建站点并自动发布。

注意：GitHub Pages 公开站点即使源仓库是 Private 也不能自动获得隐私保护；不要公开 API Key 等敏感资料。

官方参考：
- https://www.mkdocs.org/user-guide/writing-your-docs/
- https://squidfunk.github.io/mkdocs-material/publishing-your-site/
- https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site
