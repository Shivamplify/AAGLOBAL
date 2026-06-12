import os, json
files = {}
for root, dirs, fnames in os.walk(r'C:\Users\codex\.gemini\antigravity'):
    if 'transcript.jsonl' in fnames:
        log_path = os.path.join(root, 'transcript.jsonl')
        for line in open(log_path, 'r', encoding='utf-8'):
            try:
                step = json.loads(line)
                if step.get('type') == 'PLANNER_RESPONSE':
                    for tool in step.get('tool_calls', []):
                        if tool['name'] == 'write_to_file':
                            args = tool.get('args', {})
                            path = args.get('TargetFile', '')
                            if 'admin' in path:
                                files[path.replace('\\\\', '\\').strip('"')] = args.get('CodeContent', '').strip('"')
            except Exception as e:
                pass
print('Found:', list(files.keys()))
for path, content in files.items():
    try:
        if content:
            # Reconstruct unicode
            content = content.encode('raw_unicode_escape').decode('unicode_escape')
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
    except Exception as e:
        print(e)
