import re
from pathlib import Path

docs_dir = Path("g:/github/tg-evp/docs")

for md_file in docs_dir.glob("*.md"):
    if md_file.name == "index.md":
        continue
    
    content = md_file.read_text(encoding='utf-8')
    
    # Заменяем TOML frontmatter (+++) на YAML (---)
    # Проверяем, начинается ли файл с +++
    if content.startswith('+++'):
        # Находим закрывающий +++
        end_match = re.search(r'^\+\+\+\n(.*?)\n\+\+\+', content, re.DOTALL | re.MULTILINE)
        if end_match:
            frontmatter = end_match.group(1)
            # Заменяем +++ на ---
            new_content = re.sub(r'^\+\+\+\n(.*?)\n\+\+\+', r'---\n\1\n---', content, flags=re.DOTALL | re.MULTILINE)
            md_file.write_text(new_content, encoding='utf-8')
            print(f"✓ {md_file.name}")

print("Готово! Все файлы конвертированы в YAML frontmatter.")