---
---

# Архив постов из Telegram-канала "Елена Панина"

Всего файлов: {{ site.pages | where_exp: "item", "item.path contains '.md'" | size | minus: 1 }}

<ul>
{% for page in site.pages %}
  {% if page.path contains '.md' and page.path != 'index.md' %}
    <li><a href="{{ page.url | relative_url }}">{{ page.name }}</a></li>
  {% endif %}
{% endfor %}
</ul>