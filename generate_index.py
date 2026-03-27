import os
from pathlib import Path

docs_dir = Path("g:/github/tg-evp/docs")
files = sorted(docs_dir.glob("*.md"))

html = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Архив текстов — Елена Панина</title>
    <style>
        body { font-family: 'Segoe UI', sans-serif; margin: 20px; background: #f5f5f5; }
        .container { max-width: 800px; margin: 0 auto; background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        h1 { color: #333; border-bottom: 2px solid #eee; padding-bottom: 10px; }
        .files { display: flex; flex-direction: column; gap: 5px; margin-top: 20px; }
        a { color: #0366d6; text-decoration: none; font-family: monospace; }
        a:hover { text-decoration: underline; }
        .counter { background: #e1e4e8; padding: 5px 10px; border-radius: 20px; font-size: 14px; display: inline-block; margin-bottom: 10px; }
        hr { margin: 20px 0; border: none; border-top: 1px solid #eee; }
    </style>
</head>
<body>
<div class="container">
    <h1>📄 Архив текстов</h1>
    <div class="counter">Всего файлов: """ + str(len(files)) + """</div>
    <div class="files">
"""

for f in files:
    html += f'        <a href="{f.name}">{f.name}</a>\n'

html += """    </div>
    <hr>
    <p style="color: #666; font-size: 12px;">Автоматически сгенерированный список</p>
</div>
</body>
</html>
"""

with open(docs_dir / "index.html", "w", encoding="utf-8") as f:
    f.write(html)

print(f"✅ Создан index.html с {len(files)} файлами")