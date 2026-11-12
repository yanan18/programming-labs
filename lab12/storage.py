import json

def load_records(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if type(data) is not list:
                return []
            return data
    except:
        return []

def save_records(path, records):
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(records, f, ensure_ascii=False, indent=2)
        return True
    except:
        return False
