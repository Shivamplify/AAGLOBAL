import json
log_path = r'C:\Users\codex\.gemini\antigravity\brain\752d3689-f268-4463-a8ed-791a9fddd4d5\.system_generated\logs\transcript.jsonl'

bot_py_content = None
bot_html_content = None

for line in open(log_path, 'r', encoding='utf-8'):
    try:
        step = json.loads(line)
        if step.get('type') == 'PLANNER_RESPONSE':
            dt_str = step['created_at']
            if '2026-06-11' in dt_str:
                for tool in step.get('tool_calls', []):
                    if tool['name'] == 'write_to_file':
                        target = tool['args'].get('TargetFile', '')
                        if 'bot.py' in target:
                            bot_py_content = tool['args'].get('CodeContent', '')
                        if 'bot_control.html' in target:
                            bot_html_content = tool['args'].get('CodeContent', '')
                    elif tool['name'] in ['replace_file_content', 'multi_replace_file_content']:
                        # Also apply any replacements that happened on June 11
                        target = tool['args'].get('TargetFile', '')
                        if 'bot.py' in target:
                            if tool['name'] == 'replace_file_content':
                                bot_py_content = bot_py_content.replace(tool['args'].get('TargetContent', ''), tool['args'].get('ReplacementContent', ''))
    except Exception:
        pass

if bot_py_content:
    with open(r'c:\Users\codex\OneDrive\Desktop\blognews\app\bot.py', 'w', encoding='utf-8') as f:
        f.write(bot_py_content)
    print('Restored bot.py')

if bot_html_content:
    with open(r'c:\Users\codex\OneDrive\Desktop\blognews\app\templates\admin\bot_control.html', 'w', encoding='utf-8') as f:
        f.write(bot_html_content)
    print('Restored bot_control.html')
