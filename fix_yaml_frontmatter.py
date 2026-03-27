import re
from pathlib import Path

# Укажите путь к папке docs
docs_dir = Path("g:/github/tg-evp/docs")

print("🔧 Исправление YAML frontmatter в MD-файлах...")
print(f"📁 Папка: {docs_dir}\n")

for md_file in docs_dir.glob("*.md"):
    if md_file.name == "index.md":
        continue
    
    original = md_file.read_text(encoding='utf-8')
    
    # Проверяем, есть ли YAML frontmatter (--- ... ---)
    match = re.search(r'^---\n(.*?)\n---', original, re.DOTALL | re.MULTILINE)
    if not match:
        continue
    
    frontmatter = match.group(1)
    new_frontmatter = re.sub(r'(\w+)\s*=\s*', r'\1: ', frontmatter)
    
    if frontmatter == new_frontmatter:
        continue
    
    new_content = original.replace(frontmatter, new_frontmatter, 1)
    md_file.write_text(new_content, encoding='utf-8')
    print(f"✓ {md_file.name}")

print("\n✅ Готово!")