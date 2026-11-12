import json

def validate_todos(data):
    if type(data) is not list:
        raise ValueError("Корень должен быть списком")
    
    ids = set()
    for item in data:
        if type(item) is not dict:
            raise ValueError("Запись должна быть словарем")
            
        if "id" not in item or type(item["id"]) is not int or item["id"] <= 0:
            raise ValueError("Неверный id")
        if item["id"] in ids:
            raise ValueError("id должен быть уникальным")
        ids.add(item["id"])
        
        if "userId" not in item or type(item["userId"]) is not int or item["userId"] <= 0:
            raise ValueError("Неверный userId")
            
        if "title" not in item or type(item["title"]) is not str or item["title"] == "":
            raise ValueError("Неверный title")
            
        if "completed" not in item or type(item["completed"]) is not bool:
            raise ValueError("Неверный completed")

def completion_counts(todos):
    counts = {}
    for item in todos:
        user = item["userId"]
        if user not in counts:
            counts[user] = 0
        if item["completed"] == True:
            counts[user] += 1
    return counts

def top_users(counts):
    if len(counts) == 0:
        return []
    
    max_count = max(counts.values())
    if max_count == 0:
        return []
        
    result = []
    for user in counts:
        if counts[user] == max_count:
            result.append(user)
    return sorted(result)

def select_tasks(todos, user_id, parameter=None):
    result = []
    for item in todos:
        if item["userId"] == user_id:
            if parameter is None:
                result.append(item["id"])
            else:
                if parameter.lower() in item["title"].lower():
                    result.append(item["id"])
    return result
