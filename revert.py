import json

log_path = r'C:\Users\codex\.gemini\antigravity\brain\752d3689-f268-4463-a8ed-791a9fddd4d5\.system_generated\logs\transcript.jsonl'
reversions = []

with open(log_path, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            step = json.loads(line)
            if step.get('type') == 'PLANNER_RESPONSE':
                dt_str = step['created_at']
                # Target changes made today (June 12th after 03:00 UTC)
                if '2026-06-12T03' in dt_str or '2026-06-12T04' in dt_str:
                    for tool in step.get('tool_calls', []):
                        name = tool['name']
                        if name in ['replace_file_content', 'multi_replace_file_content']:
                            args = tool.get('args', {})
                            target = args.get('TargetFile', '').strip('\"').replace('\\\\', '\\')
                            if name == 'replace_file_content':
                                old_content = args.get('TargetContent', '')
                                new_content = args.get('ReplacementContent', '')
                                reversions.append((target, new_content, old_content))
                            elif name == 'multi_replace_file_content':
                                for chunk in args.get('ReplacementChunks', []):
                                    old_content = chunk.get('TargetContent', '')
                                    new_content = chunk.get('ReplacementContent', '')
                                    reversions.append((target, new_content, old_content))
        except Exception:
            pass

reversions.reverse()

for target, new_content, old_content in reversions:
    try:
        with open(target, 'r', encoding='utf-8') as f:
            content = f.read()
        if new_content in content:
            content = content.replace(new_content, old_content)
            with open(target, 'w', encoding='utf-8') as f:
                f.write(content)
            print('Reverted in', target.split('blognews')[-1])
        else:
            print('Could not find new_content in', target.split('blognews')[-1])
    except Exception as e:
        print('Error with', target, e)
