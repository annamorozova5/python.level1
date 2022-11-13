import json

with open('file.json', 'r', encoding='utf8') as f:
    text = json.load(f)
    print(text)
for txt in text['personal']:
    print(txt['name'], ':', txt['age'])
