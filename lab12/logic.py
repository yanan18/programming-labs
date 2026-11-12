def validate_records(records):
    ids = []
    for r in records:
        if type(r) is not dict:
            raise ValueError("Запись должна быть словарем")
        if "id" not in r or type(r["id"]) is not int or r["id"] <= 0:
            raise ValueError("Неверный id")
        if r["id"] in ids:
            raise ValueError("Повторяющийся id")
        ids.append(r["id"])
        
        if "title" not in r or type(r["title"]) is not str or r["title"].strip() == "":
            raise ValueError("Неверный title")
        if "category" not in r or type(r["category"]) is not str or r["category"].strip() == "":
            raise ValueError("Неверный category")
        if "amount" not in r or type(r["amount"]) is not int or r["amount"] < 0:
            raise ValueError("Неверный amount")
        if "completed" not in r or type(r["completed"]) is not bool:
            raise ValueError("Неверный completed")

def add_record(records, title, category, amount):
    if len(records) == 0:
        new_id = 1
    else:
        max_id = 0
        for r in records:
            if r["id"] > max_id:
                max_id = r["id"]
        new_id = max_id + 1
        
    new_record = {
        "id": new_id,
        "title": title.strip(),
        "category": category.strip(),
        "amount": amount,
        "completed": False
    }
    records.append(new_record)
    return new_record

def find_records(records, query):
    if query.strip() == "":
        return []
    result = []
    for r in records:
        if query.strip().lower() in r["title"].lower():
            result.append(r)
    return result

def set_completed(records, record_id, completed):
    for r in records:
        if r["id"] == record_id:
            r["completed"] = completed
            return True
    return False

def delete_record(records, record_id):
    for r in records:
        if r["id"] == record_id:
            records.remove(r)
            return True
    return False

def statistics(records):
    total = len(records)
    done = 0
    not_done = 0
    sum_amount = 0
    cats = {}
    
    for r in records:
        if r["completed"] == True:
            done += 1
        else:
            not_done += 1
            
        sum_amount += r["amount"]
        
        cat = r["category"].strip()
        if cat not in cats:
            cats[cat] = 0
        cats[cat] += r["amount"]
        
    return total, done, not_done, sum_amount, cats
