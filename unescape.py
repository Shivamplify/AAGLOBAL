import json
import codecs

def unescape(content):
    if content.startswith('"') and content.endswith('"'):
        try:
            return json.loads(content)
        except:
            return codecs.decode(content[1:-1], 'unicode_escape')
    return content

with open(r'c:\Users\codex\OneDrive\Desktop\blognews\app\bot.py', 'r', encoding='utf-8') as f:
    bot = unescape(f.read())
with open(r'c:\Users\codex\OneDrive\Desktop\blognews\app\bot.py', 'w', encoding='utf-8') as f:
    f.write(bot)

with open(r'c:\Users\codex\OneDrive\Desktop\blognews\app\templates\admin\bot_control.html', 'r', encoding='utf-8') as f:
    bot_html = unescape(f.read())
with open(r'c:\Users\codex\OneDrive\Desktop\blognews\app\templates\admin\bot_control.html', 'w', encoding='utf-8') as f:
    f.write(bot_html)
