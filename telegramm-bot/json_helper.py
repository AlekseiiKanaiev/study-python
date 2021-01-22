import json

def write_json(data, filename = 'telegramm-bot/answer.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
