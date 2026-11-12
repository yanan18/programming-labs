import json
import os
from analysis import validate_todos, completion_counts, top_users, select_tasks

os.chdir(os.path.dirname(os.path.abspath(__file__)))

try:
    with open("todos.json", "r", encoding="utf-8") as f:
        todos = json.load(f)
        
    validate_todos(todos)
    print("Файл прочитан и проверен.")
    
    counts = completion_counts(todos)
    print("Выполнено задач по пользователям:", counts)
    
    leaders = top_users(counts)
    print("Лидеры:", leaders)
    
    leaders_tasks = []
    for t in todos:
        if t["userId"] in leaders and t["completed"] == True:
            leaders_tasks.append(t["id"])
            
    with open("leaders.json", "w", encoding="utf-8") as f:
        json.dump(leaders_tasks, f, ensure_ascii=False, indent=2)
    print("Сохранено в leaders.json")
    
    user_id = int(input("Введите ID пользователя: "))
    param = input("Введите подстроку для поиска: ")
    
    selected = select_tasks(todos, user_id, param)
    print("Найденные задачи:", selected)
    
    with open("selected.json", "w", encoding="utf-8") as f:
        json.dump(selected, f, ensure_ascii=False, indent=2)
    print("Сохранено в selected.json")
        
except Exception as e:
    print("Ошибка:", e)
