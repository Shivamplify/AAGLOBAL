import json, re, os

log_path = r'C:\Users\codex\.gemini\antigravity\brain\752d3689-f268-4463-a8ed-791a9fddd4d5\.system_generated\logs\transcript.jsonl'
files = {}
for line in open(log_path, 'r', encoding='utf-8'):
    try:
        step = json.loads(line)
        if step.get('type') == 'PLANNER_RESPONSE':
            for tool in step.get('tool_calls', []):
                if tool['name'] == 'write_to_file':
                    args = tool.get('args', {})
                    path = args.get('TargetFile', '').strip('\"')
                    if r'app\templates\admin' in path or 'app/templates/admin' in path:
                        files[path.replace('\\\\', '\\')] = args.get('CodeContent', '').strip('\"')
    except Exception as e:
        pass

print('Found files:', list(files.keys()))
for path, content in files.items():
    print('Restoring', path)
    try:
        content = content.encode('raw_unicode_escape').decode('unicode_escape')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
    except Exception as e:
        print('Error:', e)
