import re
from pathlib import Path

docs_dir = Path("g:/github/tg-evp/docs")

for md_file in docs_dir.glob("*.md"):
    if md_file.name == "index.md":
        continue
    
    content = md_file.read_text(encoding='utf-8')
    
    # Заменяем T на пробел
    # date: 2026-03-20T16:33:01 -> date: 2026-03-20 16:33:01
    new_content = re.sub(r'(date:\s*)(\d{4}-\d{2}-\d{2})T(\d{2}:\d{2}:\d{2})', r'\1\2 \3', content)
    
    if new_content != content:
        md_file.write_text(new_content, encoding='utf-8')
        print(f"✓ {md_file.name}")

print("Готово!")