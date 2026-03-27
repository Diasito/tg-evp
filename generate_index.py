# g:\github\tg-evp\generate_index.py
import os
from pathlib import Path

# Папка с MD-файлами
docs_dir = Path("g:/github/tg-evp/docs")

# Собираем все MD-файлы
files = sorted([f.name for f in docs_dir.glob("*.md") if f.name != "index.html"])

# Генерируем HTML
html = f'''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Архив текстов — Елена Панина</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1>📄 Архив текстов</h1>
        <p>Всего файлов: <strong>{len(files)}</strong></p>
        <hr>
        <ul>
'''

for f in files:
    html += f'            <li><a href="{f}">{f}</a></li>\n'

html += '''        </ul>
    </div>
</body>
</html>
'''

# Сохраняем
index_path = docs_dir / "index.html"
index_path.write_text(html, encoding='utf-8')

print(f"✅ Создан index.html с {len(files)} файлами")
print(f"📁 {index_path}")