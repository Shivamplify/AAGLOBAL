import re
with open(r'c:\Users\codex\OneDrive\Desktop\blognews\app\templates\base.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove google translate div and scripts
content = re.sub(r'<div id="google_translate_element".*?</script>', '', content, flags=re.DOTALL)
# Remove goog-te-banner-frame css
content = re.sub(r'/\* Hide Google Translate Banner and tooltips \*/.*?\}', '', content, flags=re.DOTALL)
content = re.sub(r'body \{ top: 0px !important; \}', '', content)
content = re.sub(r'\.goog-tooltip.*?\}', '', content, flags=re.DOTALL)
content = re.sub(r'\.goog-text-highlight.*?\}', '', content, flags=re.DOTALL)

# Remove the translation button in the topbar
content = re.sub(r'<div class="dropdown me-3">.*?<button class="btn btn-sm modern-lang-btn.*?</ul>\s*</div>', '', content, flags=re.DOTALL)

with open(r'c:\Users\codex\OneDrive\Desktop\blognews\app\templates\base.html', 'w', encoding='utf-8') as f:
    f.write(content)
